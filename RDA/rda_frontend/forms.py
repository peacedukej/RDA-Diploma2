from django.contrib.auth import password_validation
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

from .models import Patient


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='Обязательное поле',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'for': 'login-username'}))
    email = forms.EmailField(max_length=100, help_text='Почта необходима для восстановления доступа',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'for': 'contact-email'}))
    password1 = forms.CharField(label='Пароль', help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Ваш логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'for': 'login-username'}))
    password = forms.CharField(label='Пароль',  # help_text=password_validation.password_validators_help_text_html(),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))


class NewUserProfile(ModelForm):
    first_name = forms.CharField(help_text='Обязательное поле',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(help_text='Обязательное поле',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    patronymic = forms.CharField(help_text='При отсутствии отчества поле можно оставить пустым',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    phone = forms.CharField(help_text='Обязательное поле',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+79991234567'}))

    # birthday = forms.DateTimeField(help_text='Обязательное поле',
    #                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    # photo = forms.URLField

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'patronymic',
            'phone',
            # 'birthday',
            # 'photo',
            # 'access_group'
        ]


class EditPassword(PasswordChangeForm):
    old_password = forms.CharField(label='Текущий пароль',
                               help_text=password_validation.password_validators_help_text_html(),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))

    new_password1 = forms.CharField(label='Новый пароль',
                               help_text=password_validation.password_validators_help_text_html(),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))

    new_password2 = forms.CharField(label='Повторите новый пароль',
                               help_text=password_validation.password_validators_help_text_html(),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))
# class EditPassword(ModelForm):
#     password = forms.CharField(label='Текущий пароль',
#                                # help_text=password_validation.password_validators_help_text_html(),
#                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'for': 'login-password'}))
#     new_password1 = forms.CharField(label='Новый пароль',
#                                     # help_text=password_validation.password_validators_help_text_html(),
#                                     widget=forms.PasswordInput(
#                                         attrs={'class': 'form-control', 'for': 'login-password'}))
#
#     new_password2 = forms.CharField(label='Повторите новый пароль',
#                                     # help_text=password_validation.password_validators_help_text_html(),
#                                     widget=forms.PasswordInput(
#                                         attrs={'class': 'form-control', 'for': 'login-password'}))
#
#     class Meta:
#         model = User
#         fields = [
#             'password',
#         ]

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
