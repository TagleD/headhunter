from django import forms
from django.contrib.auth import get_user_model


class CustomAccountCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True, widget=forms.PasswordInput)


    class Meta:
        model = get_user_model()
        fields = ('user_type', 'name', 'email', 'password', 'password_confirm', 'phone', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data.get('password'))
        if commit:
            account.save()
            get_user_model().objects.get_or_create(account=account)
        return account