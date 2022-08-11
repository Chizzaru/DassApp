from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'lastname',
            'firstname',
            'middlename',
            'address',
            'email',
            'dateofbirth',
            'contact',
            'gender'
        ]