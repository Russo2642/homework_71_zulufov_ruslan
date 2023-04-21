from api.serializers import PostSerializer, LikeSerializer
from posts.models import Like
from posts.models import Post
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.permissions import PostPermission


class PostView(ModelViewSet):
    permission_classes = [PostPermission, IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
