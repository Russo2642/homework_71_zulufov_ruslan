from django.contrib import admin

from posts.models import Post, Comment, Like


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'author', 'created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
