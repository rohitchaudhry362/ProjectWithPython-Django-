# Generated by Django 2.1.3 on 2019-02-10 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0042_auto_20190210_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liborderdetails',
            old_name='DateOfOrder',
            new_name='Date',
        ),
    ]