from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse


# Create your views here.



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def account(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_url')

    else:
     form=UserCreationForm()
    return render(request, "account.html")
    return render(request, "account.html")

def blog(request):
    return render(request, "blog.html")
    
def cart(request):
    return render(request, "cart.html")

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
    return render(request, "single-product.html")

def login(request):
    return render(request, "login.html")


