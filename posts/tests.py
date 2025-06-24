from http.client import responses

from rest_framework.test import  APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from .models import *

User = get_user_model()

class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.post = Post.objects.create(
            user = self.user,
            title = 'title',
            caption = 'caption',
            is_active = True,
            is_public = True,
        )

    def test_post_creation(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.post.title, 'title')
        self.assertEqual(self.post.is_public, True)

    def test_postfile_creation(self):
        postfile = PostFile.objects.create(post=self.post, file='fake/path/to/file/jpg')
        self.assertEqual(PostFile.objects.count(), 1)
        self.assertEqual(postfile.post, self.post)


    def test_comment_creation(self):
        comment = Comment.objects.create(
            post = self.post,
            user = self.user,
            comment = 'comment',
            is_approved = True
        )
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.comment, 'comment')

    def test_like_creation(self):
        like = Like.objects.create(
            post = self.post,
            user = self.user,
            is_liked = True
        )

        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(like.is_liked, True)



class APITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.post = Post.objects.create(
            user = self.user,
            title = 'title',
            caption = 'caption'
        )

    def test_get_single_post(self):
        url = f'/api/posts/{self.post.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_create_post(self):
        url = '/api/posts/'
        data = {
            "title": "title",
            "caption": "caption",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_list_post(self):
        # url = f'/api/post/comments/{self.post.pk}/'
        url = f'/api/posts/{self.post.pk}/comments/'
        data = {
            "comment": "comment",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comment'], "comment")

    def test_get_like(self):
        Like.objects.create(post=self.post, user=self.user, is_liked=True)
        # url = f'/api/post/like/{self.post.pk}/'
        url = f'/api/posts/{self.post.pk}/likes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['likes'], 1)

    def test_add_like(self):
        url = f'/api/posts/{self.post.pk}/likes/'
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
