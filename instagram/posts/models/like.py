from django.contrib.auth import get_user_model
from django.db import models

from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        blank=True,
        null=True,
        related_name='likes',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to=Post,
        blank=True,
        null=True,
        related_name='likes',
        verbose_name='Пост',
        on_delete=models.CASCADE,
    )
