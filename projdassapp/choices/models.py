from django.db import models

class Choice(models.Model):
    point = models.IntegerField()
    detail = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']