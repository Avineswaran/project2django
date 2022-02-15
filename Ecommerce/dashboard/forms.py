from unicodedata import category
from django import forms
from .models import WeeklyProfit
from .models import Markup

class WeeklyProfitForm(forms.ModelForm):
    week    = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    profit  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    class Meta:
        model = WeeklyProfit
        fields = ('week','profit')

class MarkupModelForm(forms.ModelForm):
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}))
    percentage_value = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Markup
        fields = ('category','percentage_value')