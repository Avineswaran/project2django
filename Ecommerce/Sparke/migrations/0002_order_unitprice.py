# Generated by Django 3.2.9 on 2022-01-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unitprice',
            field=models.FloatField(null=True),
        ),
    ]
