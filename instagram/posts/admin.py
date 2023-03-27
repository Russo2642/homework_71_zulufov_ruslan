from django.contrib import admin

from posts.models import Post

from posts.models import Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'author', 'created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
