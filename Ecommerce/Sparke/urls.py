from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('',views.base,name="base"),
    path('',views.login,name="login"),
    path('',views.PartTest,name="PartTest")
]