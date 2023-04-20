from rest_framework.viewsets import ModelViewSet

from posts.models import Post

from api.serializers import PostSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
