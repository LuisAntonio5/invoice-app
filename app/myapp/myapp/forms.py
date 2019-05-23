from django.forms import ModelForm
from .models import Invoice
from django.db import models

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['fromm','to', 'title', 'value']
