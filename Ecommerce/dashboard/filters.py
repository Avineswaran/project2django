import django_filters
from django import forms
from .models import Invoice

class InvoiceFilter(django_filters.FilterSet):
    class Meta:
        model = Invoice
        fields = {
            'invoiceNo' : ['icontains'],
        }