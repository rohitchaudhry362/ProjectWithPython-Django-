# Generated by Django 2.1.3 on 2019-02-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190217_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('enroll', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=30, unique=True)),
                ('sem', models.IntegerField()),
                ('stream', models.CharField(choices=[('Computer', 'COM_SCIENCE'), ('Chemical', 'CHEMICAL'), ('Mechanical', 'MECHANICAL'), ('Civil', 'CIVIL')], max_length=30)),
            ],
        ),
    ]
