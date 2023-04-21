from django.contrib.auth import get_user_model
from django.db import models

from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        blank=False,
        null=False,
        related_name='likes',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to=Post,
        blank=False,
        null=False,
        related_name='likes',
        verbose_name='Пост',
        on_delete=models.CASCADE,
    )
