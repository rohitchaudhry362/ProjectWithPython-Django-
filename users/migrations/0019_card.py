# Generated by Django 2.1.3 on 2019-03-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_student_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('enroll', models.IntegerField(primary_key=True, serialize=False)),
                ('isblocked', models.BooleanField(default=False)),
            ],
        ),
    ]
