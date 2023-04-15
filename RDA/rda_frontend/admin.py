from django.contrib import admin
from .models import Patient, Doctor, UserDoctor, Disease, UserDisease, Files, Analysis, AnalysisFields
# Register your models here.


class AnalysisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Analysis._meta.get_fields()]

class AnalysisFieldsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnalysisFields._meta.get_fields()]

class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.get_fields()]

admin.site.register(Patient, PatientAdmin)
# admin.site.register(UserInfo)
admin.site.register(Doctor)
admin.site.register(UserDoctor)
admin.site.register(Disease)
admin.site.register(UserDisease)
admin.site.register(Files)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(AnalysisFields, AnalysisFieldsAdmin)