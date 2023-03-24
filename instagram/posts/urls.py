from django.urls import path

from posts.views.base import IndexView

from posts.views.posts import PostCreateView, PostDetailView, AddLike, AddComments


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/add/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/like', AddLike.as_view(), name='add_like'),
    path('post/<int:pk>/comment', AddComments.as_view(), name='add_comments')
]
