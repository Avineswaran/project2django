
from django.db import connections, models
from django.contrib.auth.models import User

# Create your models here.


class Part(models.Model):
    image = models.TextField(blank=True, null=True)
    partno = models.CharField(db_column='partNo', primary_key=True, max_length=15)  # Field name made lowercase.
    partname = models.CharField(db_column='partName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    partcategory = models.CharField(db_column='partCategory', max_length=30, blank=True, null=True)  # Field name made lowercase.
    partyear = models.DateField(db_column='partYear', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'
    

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Cart(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField()
    productid = models.CharField(db_column='productId', max_length=15)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=40)  # Field name made lowercase.
    quantity = models.IntegerField()
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'

class Customer(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phoneno = models.CharField(db_column='phoneNo', primary_key=True, max_length=15)  # Field name made lowercase.
    custid = models.CharField(db_column='custID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    streetaddr = models.CharField(db_column='streetAddr', max_length=40, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=25, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'