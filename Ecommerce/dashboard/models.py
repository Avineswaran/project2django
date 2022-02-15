from django.db import models
from django.urls import reverse

# Create your models here.
class WeeklyProfit(models.Model):
    week = models.IntegerField(unique=True)
    profit = models.FloatField()

    class Meta:
        ordering = ['week']

    def __str__(self):
        return "{}-{}".format(self.week, self.profit)

class Markup(models.Model):
    category = models.CharField(max_length=100, null=True) 
    percentage_value = models.FloatField()

    def get_absolute_url(self):
        return reverse ("dashboards:update_markup", kwargs={"id": self.id})

class Invoice(models.Model):
    invoiceNo = models.CharField(max_length=100) 
    paymentID = models.CharField(max_length=100) 
    orderID = models.CharField(max_length=100) 
    invoiceDate = models.DateTimeField(null=True)
    custPhone = models.CharField(max_length=100) 
    custAddr = models.CharField(max_length=100) 
    totalPayment = models.FloatField(null=True)