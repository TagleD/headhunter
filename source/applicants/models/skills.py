from django.db import models


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Навык'
    )

    def __str__(self):
        return self.name