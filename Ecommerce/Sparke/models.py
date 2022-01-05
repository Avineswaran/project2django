
from django.db import connections, models

# Create your models here.


class Part(models.Model):
    partno = models.CharField(db_column='partNo', primary_key=True, max_length=40)  # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    partcategory = models.CharField(db_column='partCategory', max_length=30, blank=True, null=True)  # Field name made lowercase.
    partyear = models.DateField(db_column='partYear', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.DecimalField(db_column='unitPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'