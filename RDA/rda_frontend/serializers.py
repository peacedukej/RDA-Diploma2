from rest_framework import serializers
from .models import Patient, Analysis, AnalysisFields


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = ('user_id', 'analysis_id', 'analysis_type', 'analysis_user_name')


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('user_id', 'first_name', 'last_name')