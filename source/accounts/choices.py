from django.db.models import TextChoices


class UserTypeChoice(TextChoices):
    APPLICANT = 'applicant', 'Соискатель'
    COMPANY = 'company', 'Работодатель'