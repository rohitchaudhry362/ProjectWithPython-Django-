# Generated by Django 2.1.3 on 2019-02-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0035_auto_20190210_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='liborderdetails',
            name='DateOfOrder',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
