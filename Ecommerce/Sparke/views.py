from allauth.account.forms import SignupForm
from django.shortcuts import render,redirect 
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .models import Cart, Customer, Part 
from django.http import JsonResponse
import json 
from .models import Part, Cart
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import Profileform, form_validation_error 

# Create your views here.



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def account(request):
    return render(request, "account.html")

def myaccount(request):
    return render(request, "myaccount.html")

def blog(request):
    return render(request, "blog.html")

def base1(request):
    return render(request, "base1.html")

def seller(request):
    return render(request, "seller.html")
    

def update(request):
    return render(request, "update.html")

def signup1(request):
    return render(request, "signup1.html")

def blogdetail(request):
    return render(request, "blog-detail.html")

def shopv1rootcategory(request):
    return render(request, "shopv1rootcategory.html")

def shopv2subcategory(request):
    return render(request, "shopv2subcategory.html")

def losspassword(request):
    return render(request, "loss-password.html")

def shopv3subsubcategory(request):
    return render(request, "shopv3subsubcategory.html")

def shopv4filterascategory(request):
    return render(request, "shopv4filterascategory.html")

def shopv5productnotfound(request):
    return render(request, "shopv5productnotfound.html")

def shopv6searchresults(request):
    return render(request, "shopv6searchresults.html")

def wishlist(request):
    return render(request, "wishlist.html")

def wishlistempty(request):
    return render(request, "wishlist-empty.html")

def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

def custom(request):
    return render(request, "custom.html")

def faq(request):
    return render(request, "faq.html")

def error(request):
    return render(request, "error.html")

def terms(request):
    return render(request, "terms.html")

def track(request):
    return render(request, "track.html")

def store(request):
    return render(request, "store.html")

def lostpassword(request):
    return render(request, "lost-password.html")

def cartempty(request):
    return render(request, "cartempty.html")

def checkout(request):
    return render(request, "checkout.html")

def confirmation(request):
    return render(request, "confirmation.html")

def homehtml(request):
    return render(request, "homehtml.html")

def singleproduct(request):
    return render(request, "singleproduct.html")

def login(request):
    return render(request, "login.html")

def base(request):
    return render(request, "base.html")

def signup(request):
    return render(request, "signup.html")

def account(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = SignupForm()
    return render(request, "account.html",{"form":form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render


def PartTest(request):
    parts = Part.objects.all()
    return render(request,"PartTest.html",{'parts':parts})


def cart(request):
    carts = Cart.objects.all()
    return render(request,"cart.html",{'carts':carts})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer = request.user.customer 
    product = Part.objects.get(id=productId)
    order, created = Cart.objects.get_or_create(customer=customer,complete=False)
    
    return JsonResponse('Item was added',safe=False)


def ProfileView(request):
    if request.method == "POST":
        form =Profileform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/profile")
    else:
        form = Profileform()
    return render(request, "profile.html",{"form":form})

