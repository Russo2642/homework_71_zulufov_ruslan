from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from posts.models import Post

from api.serializers import PostSerializer, LikeSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer

