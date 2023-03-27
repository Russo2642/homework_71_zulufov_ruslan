from django.contrib.auth.models import AbstractUser
from django.db import models


class StatusChoice(models.TextChoices):
    MALE = 'MALE', 'Мужской'
    FEMALE = 'FEMALE', 'Женский'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    about_me = models.CharField(
        null=True,
        blank=True,
        max_length=500,
        verbose_name='Обо мне'
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name='Телефон'
    )
    gender = models.CharField(
        choices=StatusChoice.choices,
        max_length=7,
        verbose_name='Пол'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
