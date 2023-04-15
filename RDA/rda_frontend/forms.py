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

    # analysis_status =

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
            # 'analysis_status'

        ]


class NewAnalysisFields(forms.ModelForm):
    value_1 = forms.CharField(label='Показатель 1', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_2 = forms.CharField(label='Показатель 2', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_3 = forms.CharField(label='Показатель 3', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_4 = forms.CharField(label='Показатель 4', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_5 = forms.CharField(label='Показатель 5', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_6 = forms.CharField(label='Показатель 6', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_7 = forms.CharField(label='Показатель 7', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_8 = forms.CharField(label='Показатель 8', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_9 = forms.CharField(label='Показатель 9', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_10 = forms.CharField(label='Показатель 10', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_11 = forms.CharField(label='Показатель 11', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_12 = forms.CharField(label='Показатель 12', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_13 = forms.CharField(label='Показатель 13', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_14 = forms.CharField(label='Показатель 14', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_15 = forms.CharField(label='Показатель 15', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_16 = forms.CharField(label='Показатель 16', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_17 = forms.CharField(label='Показатель 17', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_18 = forms.CharField(label='Показатель 18', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_19 = forms.CharField(label='Показатель 19', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_20 = forms.CharField(label='Показатель 20', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_21 = forms.CharField(label='Показатель 21', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_22 = forms.CharField(label='Показатель 22', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_23 = forms.CharField(label='Показатель 23', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_24 = forms.CharField(label='Показатель 24', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_25 = forms.CharField(label='Показатель 25', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_26 = forms.CharField(label='Показатель 26', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_27 = forms.CharField(label='Показатель 27', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_28 = forms.CharField(label='Показатель 28', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_29 = forms.CharField(label='Показатель 28', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))
    value_30 = forms.CharField(label='Показатель 30', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control add-analysis-results', 'placeholder': 'abdfb'}))

    # field_1, field_2, field_3, field_4, field_5, \
    # field_6, field_7, field_8, field_9, field_10, \
    # field_11, field_12, field_13, field_14, field_15, \
    # field_16, field_17, field_18, field_19, field_20, \
    # field_21, field_22, field_23, field_24, field_25, \
    # field_26, field_27, field_28, field_29, field_30 = 'Показатель 1', 'Показатель 2', 'Показатель 3', 'Показатель 4', 'Показатель 5', \
    #                                                    'Показатель 6', 'Показатель 7', 'Показатель 8', 'Показатель 9', 'Показатель 10', \
    #                                                    'Показатель 11', 'Показатель 12', 'Показатель 13', 'Показатель 14', 'Показатель 15', \
    #                                                    'Показатель 16', 'Показатель 17', 'Показатель 18', 'Показатель 19', 'Показатель 20', \
    #                                                    'Показатель 21', 'Показатель 22', 'Показатель 23', 'Показатель 24', 'Показатель 25', \
    #                                                    'Показатель 26', 'Показатель 27', 'Показатель 28', 'Показатель 29', 'Показатель 30'
    class Meta:
        model = AnalysisFields

        fields = [
            'value_1', 'value_2', 'value_3', 'value_4', 'value_5',
            'value_6', 'value_7', 'value_8', 'value_9', 'value_10',
            'value_11', 'value_12', 'value_13', 'value_14', 'value_15',
            'value_16', 'value_17', 'value_18', 'value_19', 'value_20',
            'value_21', 'value_22', 'value_23', 'value_24', 'value_25',
            'value_26', 'value_27', 'value_28', 'value_29', 'value_30',

            # 'field_1', 'field_2', 'field_3', 'field_4', 'field_5',
            # 'field_6', 'field_7', 'field_8', 'field_9', 'field_10',
            # 'field_11', 'field_12', 'field_13', 'field_14', 'field_15',
            # 'field_16', 'field_17', 'field_18', 'field_19', 'field_20',
            # 'field_21', 'field_22', 'field_23', 'field_24', 'field_25',
            # 'field_26', 'field_27', 'field_28', 'field_29', 'field_30',
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
