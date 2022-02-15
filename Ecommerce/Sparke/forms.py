
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from .models import Customer
 
 

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address','city','postalCode','state']
        


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


class LoginForm(forms.Form):
    """user login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())