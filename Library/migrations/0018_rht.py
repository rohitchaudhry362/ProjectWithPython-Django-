# Generated by Django 2.1.3 on 2019-01-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0017_auto_20190101_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='rht',
            fields=[
                ('rhtid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
