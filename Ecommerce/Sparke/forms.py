from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from .models import Customer
 
 
class CustomSignupForm(SignupForm):
    
    # add more fields here 
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['last_name'] = forms.CharField(required=True)
        self.fields['phonenum'] = forms.CharField(required=True)
        self.fields['strtAddr'] = forms.CharField(required=True)
        self.fields['city'] = forms.CharField(required=True)
        self.fields['postalcode'] = forms.CharField(required=True)

    class Meta:
        model = get_user_model

 
    def save(self, request):
        first_name = self.cleaned_data.pop('first_name')
        last_name = self.cleaned_data.pop('last_name')
        phonenum = self.cleaned_data.pop('phonenum')
        strtAddr = self.cleaned_data.pop('strtAddr')
        city = self.cleaned_data.pop('city')
        postalcode = self.cleaned_data.pop('postalcode')
        ...
        user = super(CustomSignupForm, self).save(request)
        return user 

class Profileform(forms.ModelForm):
    phoneno = models.CharField(max_length=15)  # Field name made lowercase.
    custid = models.CharField(max_length=15)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    streetaddr = models.CharField(max_length=40)  # Field name made lowercase.
    city = models.CharField(max_length=25)
    postalcode = models.CharField(max_length=5)  # Field name made lowercase.
    state = models.CharField(max_length=20)

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg