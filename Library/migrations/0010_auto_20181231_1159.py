# Generated by Django 2.1.3 on 2018-12-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0009_auto_20181230_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Edition',
            field=models.IntegerField(blank=True, default=True),
        ),
    ]
