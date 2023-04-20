from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Электронная Почта', widget=forms.EmailInput)
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomAccountCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput, initial='')
    password_confirm = forms.CharField(label='Подтверждение пароля', strip=False, required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('user_type', 'name', 'email', 'phone', 'password', 'password_confirm', 'avatar')
        labels = {
            'user_type': 'Выберите тип пользователя',
            'name': 'Полное имя соискателя',
            'email': 'Емэйл',
            'phone': 'Телефон',
            'password': 'Пароль',
            'password_confirm': 'Подтверждение пароля',
            'avatar': 'Аватар',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user