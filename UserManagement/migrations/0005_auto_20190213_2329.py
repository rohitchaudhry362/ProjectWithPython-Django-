# Generated by Django 2.1.3 on 2019-02-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0004_auto_20190213_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(max_length=30),
        ),
    ]
