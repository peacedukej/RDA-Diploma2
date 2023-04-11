from django.contrib.auth import password_validation
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# from .models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='Обязательное поле',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'for':'login-username'}))
    email = forms.EmailField(max_length=100, help_text='Почта необходима для восстановления доступа',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'for':'contact-email'}))
    password1 = forms.CharField(label='Пароль', help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'for':'login-password'}))
    password2 = forms.CharField(label='Подтверждение пароля', help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#
#         self.fields['email'].widget.attrs\
#             .update({
#                 'placeholder': 'Введите email',
#                 'class': 'input100 border-start-0 ms-0 form-control'
#             })
#
#         self.fields['password'].widget.attrs\
#             .update({
#                 'placeholder': 'Придумайте пароль',
#                 'class': 'input100 border-start-0 ms-0 form-control'
#         })


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']