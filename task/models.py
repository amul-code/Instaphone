from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.contact_name} - {self.contact_number}"

class SpamNumber(models.Model):
    number = models.CharField(max_length=15, unique=True)
    reported_by = models.ManyToManyField(Contact, related_name='reported_by')
    def __str__(self):
        return self.number