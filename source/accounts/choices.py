from django.db.models import TextChoices


class UserTypeChoice(TextChoices):
    APPLICANT = 'applicants', 'Соискатель'
    COMPANY = 'employers', 'Работодатель'


class CategoryChoices(TextChoices):
    INFORMATION_TECHNOLOGY = 'information technology', 'Информационные технологий'
    PHARMACY = 'pharmacy', 'Фармацевтика'
    CONSTRUCTION = 'construction', 'Строительство'
    CYBERSPORT = 'cybersport', 'Киберспорт'
    RESTAURANT_BUSINESS = 'restaurant business', 'Ресторанный бизнес'
    ENERGY = 'energy', 'Энергетика'