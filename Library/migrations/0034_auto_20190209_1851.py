# Generated by Django 2.1.3 on 2019-02-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0033_liborderdetails_bookstockserial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liborderdetails',
            name='BookStockSerial',
            field=models.CharField(default='01', max_length=100),
        ),
    ]