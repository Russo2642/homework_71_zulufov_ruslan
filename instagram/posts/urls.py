from django.urls import path

from posts.views.base import IndexView

from posts.views.posts import (
    PostCreateView,
    PostDetailView,
    AddLike,
    AddComments,
    PostUpdateView,
    PostDeleteView,
    DeleteComments
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/add/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='add_like'),
    path('post/<int:pk>/comment', AddComments.as_view(), name='comments_add'),
    path('post/<int:pk>/comment/delete', DeleteComments.as_view(), name='comments_delete'),
]
