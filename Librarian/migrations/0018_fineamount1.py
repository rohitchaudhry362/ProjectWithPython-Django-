# Generated by Django 2.1.3 on 2019-02-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Librarian', '0017_auto_20190211_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='FineAmount1',
            fields=[
                ('FaId', models.AutoField(primary_key=True, serialize=False)),
                ('User', models.IntegerField(default=True)),
                ('DateOfFine', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
