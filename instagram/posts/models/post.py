from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.TextField(
        verbose_name='Описание',
        null='False',
        max_length=3000
    )
    image = models.ImageField(
        verbose_name='Фото',
        null=False,
        blank=True,
        upload_to='posts'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
