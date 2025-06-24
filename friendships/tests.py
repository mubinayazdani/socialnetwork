from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase
from .models import Friendship

User = get_user_model()

class FriendshipModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_create_friendship(self):
        friendship = Friendship.objects.create(
            request_from=self.user1,
            request_to=self.user2
        )
        self.assertEqual(Friendship.objects.count(), 1)
        self.assertFalse(friendship.is_accepted)
        self.assertEqual(friendship.request_from, self.user1)
        self.assertEqual(friendship.request_to, self.user2)

    def test_unique_friendship(self):
        Friendship.objects.create(request_from=self.user1, request_to=self.user2)
        with self.assertRaises(Exception):
            Friendship.objects.create(request_from=self.user1, request_to=self.user2)

    def test_created_updated_time(self):
        friendship = Friendship.objects.create(request_from=self.user1, request_to=self.user2)
        self.assertIsNotNone(friendship.created_time)
        self.assertIsNotNone(friendship.updated_time)


class FriendshipViewsTest(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_user_list_view(self):
        response = self.client.get('/api/friendship/user-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_send_friend_request(self):
        response = self.client.post('/api/friendship/request/', {'user': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Friendship.objects.count(), 1)


    def test_accept_friend_request(self):
        Friendship.objects.create(request_from=self.user2, request_to=self.user1, is_accepted=False)

        self.client.force_authenticate(user=self.user1)

        response = self.client.post('/api/friendship/accept/', data={'user': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_list_accept(self):
        Friendship.objects.create(request_from=self.user2, request_to=self.user1, is_accepted=False)

        self.client.force_authenticate(user=self.user1)

        response = self.client.post('/api/friendship/request-lists/', data={'user': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_friends_list_view(self):
        Friendship.objects.create(request_from=self.user1, request_to=self.user2, is_accepted=True)
        response = self.client.get('/api/friendship/friends/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
