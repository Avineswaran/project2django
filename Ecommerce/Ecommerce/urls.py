"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Sparke import views 


urlpatterns = [


 
    path('admin/', admin.site.urls),
    path('',views.home, name='home' ),    
    path('home',views.home, name='home' ),
    path('home-html',views.homehtml, name='homehtml' ),
    path('account/',views.account, name='account' ),
    path('myaccount/',views.myaccount, name='myaccount' ),
    path('login',views.login, name='login' ), 
    path('signup',views.signup, name='signup' ), 
    path('seller',views.seller, name='seller' ), 
    path('about',views.about, name='about' ), 
    path('contact',views.contact, name='contact' ),    
    path('blog',views.blog, name='blog'  ),
    path('cart-empty',views.cartempty, name='cart-empty'  ),
    path('cart', views.cart, name='cart'),
    path('blog-detail', views.blogdetail,name='blog-detail'),
    path('lost-password', views.lostpassword, name='lost-password'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist-empty', views.wishlistempty, name='wishlist-empty'),
    path('checkout', views.checkout, name='checkout' ),
    path('faq', views.faq, name='faq' ),
    path('terms', views.terms, name='terms' ),
    path('track', views.track, name='track' ),
    path('store', views.store, name='store' ),
    path('error', views.error, name='error' ),
    path('checkout', views.checkout, name='checkout' ),
    path('custom', views.custom, name='custom' ),
    path('confirmation', views.confirmation, name='confirmation' ),
    path('singleproduct', views.singleproduct, name='singleproduct' ),
    path('base1', views.base1, name='base1' ),
    path('update', views.update, name='update' ),
    path('signup1', views.signup1, name='signup1' ),
    path('',include('Sparke.urls')),


    path('shopv1rootcategory', views.shopv1rootcategory,name='shopv1rootcategory'),
    path('shopv2subcategory', views.shopv2subcategory,name='shopv2subcategory'),
    path('shopv3subsubcategory', views.shopv3subsubcategory,name='shopv3subsubcategory'),
    path('shopv4filterascategory', views.shopv4filterascategory,name='shopv4filterascategory'),
    path('shopv5productnotfound', views.shopv5productnotfound,name='shopv5productnotfound'),
    path('shopv6searchresults', views.shopv6searchresults,name='shopv6searchresults'),
    path('PartTest',views.PartTest, name='PartTest'),

    path('',include("allauth.urls")),
]
