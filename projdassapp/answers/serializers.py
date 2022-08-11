from .models import Answer

from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='lastname'
    )

    question = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='question'
    )

    answer = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='detail'
    )

    class Meta:
        model = Answer
        fields = [
            'id',
            'patient',
            'question',
            'answer',
            'created'
        ]