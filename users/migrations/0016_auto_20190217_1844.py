# Generated by Django 2.1.3 on 2019-02-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190217_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='uniqueid',
            field=models.IntegerField(),
        ),
    ]