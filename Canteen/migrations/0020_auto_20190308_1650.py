# Generated by Django 2.1.3 on 2019-03-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0019_auto_20190308_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='quantity',
            field=models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12), ('13', 13), ('14', 14), ('15', 15)], default=1),
        ),
    ]
