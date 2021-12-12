from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def account(request):
    return render(request, "account.html")

def blog(request):
    return render(request, "blog.html")

