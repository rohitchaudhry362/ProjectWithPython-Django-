# Generated by Django 2.1.3 on 2019-02-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Librarian', '0019_fineamount1_fineamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='liborderdetails1',
            name='IsReturned',
            field=models.BooleanField(default=False),
        ),
    ]
