from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
   
    path('',views.login,name="login"),
    path('',views.PartTest,name="PartTest"),
    path('cart/',views.cart,name="cart"),
    path('/update_item/',views.updateItem,name="update_item"),
    path('profile/', views.ProfileView, name='profile'),
    path('profileEdit/', views.ProfileEdit, name='profileEdit'),
] 