from django.db import models

from patients.models import Patient
from choices.models import Choice
from questions.models import Question

class Answer(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

