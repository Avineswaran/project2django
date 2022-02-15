from django import forms
from Sparke.models import Customer

class DealerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'user',
            'name',
            'phone',
            'address',
            'city',
            'postalCode',
            'state', 
        ]