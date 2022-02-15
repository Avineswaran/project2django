# from django.http.response import JsonResponse
from django.shortcuts import render
#from django.http import JsonResponse
from django.views import View, generic
#from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import (
    PasswordChangingForm, 
    EditProfileForm, 
    #WeeklyProfitForm,
)
from django.db.models import Sum

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile_success')

    def get_object(self):
        return self.request.user

def profile_success(request):
    return render(request, 'registration/profile_success.html', {})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})