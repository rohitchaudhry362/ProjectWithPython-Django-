# Generated by Django 2.1.3 on 2019-02-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello2',
            fields=[
                ('CatId', models.AutoField(primary_key=True, serialize=False)),
                ('CatName', models.CharField(max_length=100)),
            ],
        ),
    ]
