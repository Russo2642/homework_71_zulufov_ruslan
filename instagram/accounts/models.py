from accounts.managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class StatusChoice(models.TextChoices):
    MALE = 'MALE', 'Мужской'
    FEMALE = 'FEMALE', 'Женский'


class Account(AbstractUser):
    # username = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=500,
    #     verbose_name='Логин'
    # )
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
    # password = models.CharField(
    #     null=False,
    #     blank=False,
    #     verbose_name='Пароль'
    # )
    # first_name = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=300,
    #     verbose_name='Имя'
    # )
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
        default=StatusChoice.MALE,
        max_length=7,
        verbose_name='Пол'
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившееся публикации',
        to='posts.Post',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
