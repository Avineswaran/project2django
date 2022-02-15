from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
#from chart.models import WeeklyProfit

class EditProfileForm(UserChangeForm):
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_login      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}))
    #is_superuser    = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    #is_staff        = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    #is_active       = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    date_joined     = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}))

    class Meta:
        model = User
        fields = ('email','first_name','last_name',
        'username','last_login', 'date_joined')

class PasswordChangingForm(PasswordChangeForm):
    old_password    = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password'}))
    new_password1   = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password'}))
    new_password2   = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password','new_password2')

#class WeeklyProfitForm(forms.ModelForm):
    #week    = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #profit  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    #class Meta:
        #model = WeeklyProfit
        #fields = ('week','profit')