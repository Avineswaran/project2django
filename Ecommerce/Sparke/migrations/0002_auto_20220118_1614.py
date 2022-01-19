# Generated by Django 3.2.9 on 2022-01-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparke', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='code',
            new_name='postalCode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='postalCode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='totalPrice',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='unitPrice',
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
