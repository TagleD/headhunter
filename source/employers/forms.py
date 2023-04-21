from django import forms
from django.core.exceptions import ValidationError

from .models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            'name',
            'category',
            'salary_start',
            'salary_end',
            'about',
            'requirements',
            'telegram',
            'facebook',
            'linkedin'
        )

    def clean_full_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 8:
            raise ValidationError('Полное имя должно быть длинее 8-и символов')
        return name
