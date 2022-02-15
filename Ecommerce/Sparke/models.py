from django.db import connections, models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postalCode = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
        return reverse ("dealers:dealer_detail", kwargs={"id": self.id})

class Part(models.Model):
    partNo= models.CharField(max_length=20)
    partName = models.CharField(max_length=200)
    partCategory = models.CharField(max_length=200)
    partYear= models.DateField(auto_now_add=True)
    unitPrice = models.FloatField()
    stock= models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
      return self.partName


@property
def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def shipping(self):
      shipping = True
      orderitems = self.orderitem_set.all()
      return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


class OrderItem(models.Model):
    product = models.ForeignKey(Part, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def shipping(self):
      shipping = False
      orderitems = self.orderitem_set.all()
      for i in orderitems:
        if i.product.digital == False:
          shipping = True
      return shipping

    @property
    def get_total(self):
          total = self.product.unitPrice * self.quantity
          return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	postalCode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address