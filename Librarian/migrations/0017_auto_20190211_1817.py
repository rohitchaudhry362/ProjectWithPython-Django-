# Generated by Django 2.1.3 on 2019-02-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Librarian', '0016_auto_20190211_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryorder1',
            name='DateOfOrder',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='returnbook',
            name='DateOfOrder',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='returnbook',
            name='ReturnDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]