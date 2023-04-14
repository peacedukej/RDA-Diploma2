from django.contrib.auth import password_validation
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

from .models import Patient, Analysis, AnalysisFields


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
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'for': 'login-password'}))

    new_password2 = forms.CharField(label='Повторите новый пароль',
                                    help_text=password_validation.password_validators_help_text_html(),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class NewAnalysisButton(forms.ModelForm):
#     #analysis_status = forms.CharField()
#     class Meta:
#         model = Analysis
#         fields = [
#             'analysis_status'
#         ]



class NewAnalysis(forms.ModelForm):
    # user_id = forms.IntegerField()
    # analysis_id = forms.IntegerField()
    types = [('Null', '...'),
             ('Общий анализ крови', 'Общий анализ крови'),
             ('Общий анализ мочи', 'Общий анализ мочи'),
             ('Анализ крови на С-реактивный белок', 'Анализ крови на С-реактивный белок'),
             ('Ревматоидный фактор', 'Ревматоидный фактор'),
             ('Антитела к циклическому цитруллинированному пептиду',
              'Антитела к циклическому цитруллинированному пептиду'),
             ]

    places = [('Null', '...'),
              ('Место №1', 'Место №1'),
              ('Место №2', 'Место №2'),
              ('Место №3', 'Место №3'),
              ('Место №4', 'Место №4'),
              ('Место №5', 'Место №5'),

              ]

    # class ="form-control form-select" id="add-analysis-form-select" data-bs-placeholder="..." onclick= "addAnalysisForm()" onchange="addAnalysisForm()"
    analysis_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-select',
                                                                 'placeholder': '...',
                                                                 'id': 'add-analysis-form-select',
                                                                 'onclick': "addAnalysisForm()",
                                                                 'onchange': "addAnalysisForm()"
                                                                 }
                                                          ),
                                      choices=types)
    # analysis_type = forms.CharField(
    #                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'})
    #                                )
    # date_of_upload_analysis = forms.DateField()
    place_of_analysis = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Место сдачи анализа. '
                                                                           'Можно использовать для '
                                                                           'быстрого поиска по анализам.'}),
        choices=places)

    # place_of_analysis = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Место сдачи анализа. '
    #                                                                               'Можно использовать для '
    #                                                                               'быстрого поиска по анализам.'}
    #                                )
    # )

    analysis_user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название документа, который '
                                                                              'будет отображаться в введенных '
                                                                              'анализах'}
                               )
    )

    #analysis_status =

    # date_of_analysis = forms.DateField(
    #    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'})
    # )
    class Meta:
        model = Analysis
        fields = [
            # 'user_id',
            'analysis_id',
            'analysis_type',
            # 'date_of_upload_analysis',
            'place_of_analysis',
            'analysis_user_name',
            # 'date_of_analysis',
            #'analysis_status'

        ]


class NewAnalysisFields(forms.ModelForm):
    value = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))

    class Meta:
        model = AnalysisFields

        fields = [
            # 'name',
            'value',
        ]

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
