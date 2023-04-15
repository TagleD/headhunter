from django.conf import settings
from django.db import models


class Resume(models.Model):
    applicant = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Соискатель',
        related_name='resumes',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Полное имя'
    )
    position = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name='Должность'
    )
    salary = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Желаемая зарплата'
    )
    about = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='О себе'
    )
    telegram = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Nickname telegram'
    )
    facebook = models.CharField(
        max_length=512,
        null=True,
        verbose_name='Facebook profile URL'
    )
    linkedin = models.CharField(
        max_length=512,
        null=True,
        verbose_name='Linkedin profile URL'
    )
    is_published = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        verbose_name='Статус публикации'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        null=True
    )

    def __str__(self):
        return f'{self.full_name} - {self.position[:25]}'

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
