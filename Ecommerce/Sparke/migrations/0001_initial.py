# Generated by Django 3.2.9 on 2022-01-18 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('postalCode', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sparke.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partNo', models.CharField(max_length=20)),
                ('partName', models.CharField(max_length=200)),
                ('partCategory', models.CharField(max_length=200)),
                ('partYear', models.DateField(auto_now_add=True)),
                ('unitPrice', models.FloatField()),
                ('stock', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sparke.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sparke.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitPrice', models.FloatField()),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('totalPrice', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sparke.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sparke.part')),
            ],
        ),
    ]