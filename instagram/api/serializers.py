from django.contrib.auth import get_user_model
from posts.models import Post
from rest_framework import serializers

from accounts.models import Account


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
    likes = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Post
        fields = ('id', 'author','likes')

    def update(self, instance, validated_data):
        likes = validated_data.pop('likes')
        for i in likes:
            instance.likes.add(i)
        instance.save()
        return instance
