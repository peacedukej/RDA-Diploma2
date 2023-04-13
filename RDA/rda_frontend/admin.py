from django.contrib import admin
from .models import Patient, Doctor, UserDoctor, Disease, UserDisease, Files, Analysis#, #AnalysisFields
# Register your models here.
admin.site.register(Patient)
# admin.site.register(UserInfo)
admin.site.register(Doctor)
admin.site.register(UserDoctor)
admin.site.register(Disease)
admin.site.register(UserDisease)
admin.site.register(Files)
admin.site.register(Analysis)
#admin.site.register(AnalysisFields)