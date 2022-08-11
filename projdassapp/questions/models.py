from django.db import models


class Question(models.Model):
    question = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['created']
