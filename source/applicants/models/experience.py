from django.db import models


class Experience(models.Model):
    resume = models.ForeignKey(
        'Resume',
        related_name='experiences',
        on_delete=models.CASCADE,
        verbose_name='Резюме',
    )
    company = models.CharField(
        max_length=512,
        null=False,
        blank=False,
        verbose_name='Название компании',
    )
    obligations = models.TextField(
        max_length=4096,
        null=False,
        blank=False,
        verbose_name='Описание работы',
    )
    position = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name='Занимаемая должность',
    )
    started_at = models.DateTimeField(
        verbose_name="Дата начала"
    )
    ended_at = models.DateTimeField(
        null=True,
        verbose_name='Дата окончания',
    )

    def __str__(self):
        return f'{self.company} - {self.position[:40]}'

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'
