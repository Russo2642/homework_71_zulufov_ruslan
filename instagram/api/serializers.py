from posts.models import Like
from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(default=0, read_only=True, source='likes_count')
    comments_count = serializers.SerializerMethodField(default=0, read_only=True, source='comments_count')

    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'likes_count', 'comments_count', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_likes_count(self, obj: Post):
        return obj.likes.count()

    def get_comments_count(self, obj: Post):
        return obj.comments.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post')
