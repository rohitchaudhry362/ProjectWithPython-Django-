# Generated by Django 2.1.3 on 2018-12-19 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0013_cartproduct_aggregate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='aggregate',
        ),
    ]
