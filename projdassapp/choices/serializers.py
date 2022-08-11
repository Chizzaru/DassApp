from .models import Choice

from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'point',
            'detail',
            'created'
        ]