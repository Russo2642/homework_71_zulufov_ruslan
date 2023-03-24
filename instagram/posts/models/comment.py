from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Публикация',
        to='posts.Post',
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Комментарий',
        null=False,
        blank=False,
        max_length=3000
    )
