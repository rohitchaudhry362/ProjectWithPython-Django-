# Generated by Django 2.1.3 on 2019-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0020_auto_20190308_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
