# Generated by Django 2.1.3 on 2019-02-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0028_auto_20190209_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liborderdetails',
            name='BookId',
            field=models.IntegerField(default=True),
        ),
    ]
