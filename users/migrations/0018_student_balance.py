# Generated by Django 2.1.3 on 2019-02-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
