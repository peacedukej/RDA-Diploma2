from django.contrib import admin
from .models import User, Doctor, UserDoctor, Disease, UserDisease, Files, Analysis
# Register your models here.
admin.site.register(User)
# admin.site.register(UserInfo)
admin.site.register(Doctor)
admin.site.register(UserDoctor)
admin.site.register(Disease)
admin.site.register(UserDisease)
admin.site.register(Files)
admin.site.register(Analysis)