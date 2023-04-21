from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from applicants.models import Resume, Experience


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name', 'position', 'salary', 'about', 'telegram', 'facebook', 'linkedin')

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name) < 8:
            raise ValidationError('Полное имя должно быть длинее 8-и символов')
        return full_name


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'obligations', 'position', 'started_at', 'ended_at')


experience_form_set = inlineformset_factory(
    Resume,
    Experience,
    form=ExperienceForm
)
