from django.db import models

class Patient(models.Model):
    lastname = models.CharField(max_length=100, blank=False)
    firstname = models.CharField(max_length=100, blank=False)
    middlename = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    dateofbirth = models.DateField()
    contact = models.CharField(max_length=15,blank=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.lastname+' '+self.firstname+' '+self.middlename

    class Meta:
        ordering = ['-id']
