from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import UserTypeChoice
from .managers import AccountManager


class Account(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False,
        null=False
    )

    user_type = models.CharField(
        verbose_name='Тип пользователя',
        choices=UserTypeChoice.choices,
        max_length=250,
        default=UserTypeChoice.APPLICANT
    )

    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name='Полное имя'
    )

    phone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        verbose_name='Телефон'
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
