# Generated by Django 2.1.3 on 2018-12-10 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0003_auto_20181208_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='cproduct',
            name='IsAvailable',
            field=models.BooleanField(default=True),
        ),
    ]