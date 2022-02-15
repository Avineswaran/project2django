from django.urls import path
from django.urls.resolvers import URLPattern
from Sparke import views 

urlpatterns = [
   
    path('login/',views.login,name="login"),
    path('',views.PartTest,name="PartTest"),
    path('cart/',views.cart,name="cart"),
    path('/update_item/',views.updateItem,name="update_item"),
    path('profile/', views.ProfileView, name='profile'),
    path('profileEdit/', views.ProfileEdit, name='profileEdit'),
    path("customer/login",views.LoginView.as_view(),name="customer_login"), 

] 