from django import forms
from django.core.exceptions import ValidationError

from applicants.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name', 'position', 'salary', 'about', 'telegram', 'facebook', 'linkedin')

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name) < 8:
            raise ValidationError('Полное имя должно быть длинее 8-и символов')
        return full_name