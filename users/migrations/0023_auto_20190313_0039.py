# Generated by Django 2.1.3 on 2019-03-13 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_mobile_otp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mobile',
            options={'get_latest_by': 'Pid'},
        ),
    ]
