from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.TextField(
        verbose_name='Описание',
        null='False',
        max_length=3000
    )
    image = models.ImageField(
        null=False,
        blank=True,
        upload_to='posts',
        verbose_name='Фото'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.author} - {self.description}"
