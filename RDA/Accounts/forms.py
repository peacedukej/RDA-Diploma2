from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth import login, logout, authenticate

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('email', 'password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('email', 'password')


class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']

    email = request.

class RegisterForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Введите email',
                'class': 'input100 border-start-0 ms-0 form-control'
            })

        self.fields['password'].widget.attrs\
            .update({
                'placeholder': 'Придумайте пароль',
                'class': 'input100 border-start-0 ms-0 form-control'
        })

    def clean_email(self):
        email = self.cleaned_data['email']
        if Users.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с данным email уже зарегистрирован')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password
