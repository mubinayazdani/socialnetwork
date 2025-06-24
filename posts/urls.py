from .views import PostVIEW, PostListView, CommentView, LikeView
from django.urls import path

urlpatterns = [
    path('posts/', PostVIEW.as_view()),
    path('posts/<int:pk>/', PostVIEW.as_view()),
    path('posts/', PostListView.as_view()),

    path('posts/<int:pk>/comments/', CommentView.as_view()),
    path('posts/<int:pk>/likes/', LikeView.as_view())
]