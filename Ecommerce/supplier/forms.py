from django import forms
from .models import Supplier

VEHICLE_CHOICES= [
    ('Car', 'Car'),
    ('Truck & Used Part', 'Truck & Used Part'),
    ]

BILLING_CHOICES= [
    ('E-Bill', 'E-Bill'),
    ('Hardcopy', 'Hardcopy'),
    ('Hardcopy/Scanned', 'Hardcopy/Scanned'),
    ]

TRANSACTION_CHOICES= [
    ('30 Days Term', '30 Days Term'),
    ('60 Days Term', '60 Days Term'),
    ('Cash Sale', 'Cash Sale'),
    ('TBA', 'TBA'),
    ]

class SupplierModelForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'supplierID',
            'supplierName',
            'brand',
            'partCategory',
            'vehicleType',
            'billingMethod',
            'longitude',
            'latitude',
            'transactionTerm',
            'streetAddr',
            'postalCode',
            'city',
            'state',
            'totalSupPts',
        )
        widgets={
            'supplierID': forms.TextInput(attrs={'class': 'form-control'}),
            'supplierName': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'partCategory': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicleType': forms.Select(attrs={'class': 'form-control'},choices=VEHICLE_CHOICES),
            'billingMethod': forms.Select(attrs={'class': 'form-control'},choices=BILLING_CHOICES),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'transactionTerm': forms.Select(attrs={'class': 'form-control'}, choices=TRANSACTION_CHOICES),
            'streetAddr': forms.TextInput(attrs={'class': 'form-control'}),
            'postalCode': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'totalSupPts': forms.TextInput(attrs={'class': 'form-control'}),
        }