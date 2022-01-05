from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    phonenum = forms.CharField(max_length=30, label='Phone Number',widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    strtAddr = forms.CharField(max_length=100, label='Street Address',widget=forms.TextInput(attrs={'placeholder': 'Street Address'}))
    city = forms.CharField(max_length=100, label='City', widget=forms.TextInput(attrs={'placeholder': 'City'}))
    postalcode = forms.CharField(max_length=5, label='Postal Code',widget=forms.TextInput(attrs={'placeholder': 'Postal Code'}))
    state = forms.CharField(max_length=20, label='State',widget=forms.TextInput(attrs={'placeholder': 'State'}))
    
    # add more fields here 
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user 