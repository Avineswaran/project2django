from multiprocessing import context
from re import template
from allauth.account.forms import SignupForm
from django.shortcuts import render,redirect 
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import CustomerUpdateForm
from django.urls import reverse_lazy
from .utils import *
import datetime

from .models import  Customer, Part, Order, OrderItem 
from django.http import JsonResponse
import json 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import CustomerUpdateForm, form_validation_error 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_protect



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
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, "wishlist.html",context)

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
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def confirmation(request):
    return render(request, "confirmation.html")

def homehtml(request):
    return render(request, "homehtml.html")

def singleproduct(request):
    return render(request, "singleproduct.html")

def login(request):
    return render(request, "login.html")


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
            customer = Customer(phone=None,
            name=form.cleaned_data.get('first_name')
            )
            customer.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render


def PartTest(request):
    parts = Part.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems,'parts' : parts}
    return render(request, 'PartTest.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)



@csrf_protect 
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Part.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@login_required
def ProfileView(request):
    customer = request.user.customer 
    return render(request, "profile.html",{"customer":customer})

@csrf_protect
@login_required
def ProfileEdit(request):
    if request.method == 'POST':

        c_form = CustomerUpdateForm(request.POST,instance=request.user.customer)

        context = {
            'c_form': c_form,
        }
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  
    
    else:
        
        c_form = CustomerUpdateForm(instance=request.user.customer)
        context = {'c_form':c_form} 
        return render (request, 'profileEdit.html', context)
    
    

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)