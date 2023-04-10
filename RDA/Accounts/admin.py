from django.contrib import admin

# Register your models here.

from .models import Users, Doctor, UserDoctor, Disease, UserDisease, Files, Analysis
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ['email', 'password',]



# Register your models here.
#admin.site.register(Users)
admin.site.register(Users, UsersAdmin)
# admin.site.register(UserInfo)
admin.site.register(Doctor)
admin.site.register(UserDoctor)
admin.site.register(Disease)
admin.site.register(UserDisease)
admin.site.register(Files)
admin.site.register(Analysis)