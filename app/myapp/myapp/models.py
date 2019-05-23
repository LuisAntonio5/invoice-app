from django.db import models
from django.forms import ModelForm

class Invoice(models.Model):
    fromm = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    data = models.DateField(blank=True,null=True)
