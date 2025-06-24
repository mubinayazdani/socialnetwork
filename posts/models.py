from django.conf import settings
from django.db import models

class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=2050)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.title}'


class PostFile(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField()

    class Meta:
        verbose_name = 'PostFile'
        verbose_name_plural = 'PostFiles'

    def __str__(self):
        return f'{self.pk}'

class Comment(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='comments')
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.comment}'

class Like(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'