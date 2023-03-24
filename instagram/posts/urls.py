from django.urls import path

from posts.views.base import IndexView

from posts.views.posts import PostCreateView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/add', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
