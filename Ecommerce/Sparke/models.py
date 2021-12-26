
from django.db import connections, models

# Create your models here.


class Customer(models.Model):
    phoneNo=models.CharField(max_length=15)
    dealerID=models.CharField(max_length=15)
    adminID=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    streetAddr=models.CharField(max_length=50)
    city=models.CharField(max_length=25)
    postalCode=models.CharField(max_length=5)
    state=models.CharField(max_length=20)
   
class admin(models.Model):
    pass

class part(models.Model):
    pass

class orderparts(models.Model):
    pass