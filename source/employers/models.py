from django.db import models
from django.contrib.auth import get_user_model

from accounts.choices import CategoryChoices


class Vacancy(models.Model):
    employer = models.ForeignKey(
        to=get_user_model(),
        related_name='vacancies',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Работодатель',
    )

    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Название вакансий',
    )

    category = models.CharField(
        max_length=256,
        choices=CategoryChoices.choices,
        null=False,
        blank=False,
        verbose_name='Сфера',
    )

    salary_start = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Минимальная зароботная плата'
    )

    salary_end = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Максимальная зароботная плата'
    )

    about = models.TextField(
        max_length=4096,
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    requirements = models.TextField(
        max_length=4096,
        null=True,
        blank=True,
        verbose_name='Требования',
    )

    is_published = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        verbose_name='Статус публикации'
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # LINKS
    telegram = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Nickname telegram'
    )

    facebook = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='Facebook profile URL'
    )

    linkedin = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='Linkedin profile URL'
    )

    """
        TODO:
            1. skills
            2. experience
                1. experience_start
                1. experience_end
    """

    def __str__(self):
        return f'{self.employer.name} {self.name} {self.category} {self.salary_start}-{self.salary_end}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансий'
