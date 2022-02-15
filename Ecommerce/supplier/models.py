# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class Supplier(models.Model):
    supplierID          = models.CharField(max_length=100)
    supplierName        = models.CharField(max_length=100)
    brand               = models.TextField()
    partCategory        = models.CharField(max_length=100)
    vehicleType         = models.CharField(max_length=100)
    billingMethod       = models.CharField(max_length=100)
    longitude           = models.FloatField()
    latitude            = models.FloatField()
    transactionTerm     = models.CharField(max_length=100)
    streetAddr          = models.CharField(max_length=100)
    postalCode          = models.IntegerField()
    city                = models.CharField(max_length=100)
    state               = models.CharField(max_length=100)
    totalSupPts         = models.FloatField()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse ("suppliers:supplier_detail", kwargs={"id": self.id})