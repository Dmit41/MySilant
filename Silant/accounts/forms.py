from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class AdminRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')
