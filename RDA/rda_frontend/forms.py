from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
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


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']