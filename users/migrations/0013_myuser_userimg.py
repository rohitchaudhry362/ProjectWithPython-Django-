# Generated by Django 2.1.3 on 2019-02-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190217_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='userimg',
            field=models.ImageField(blank=True, null=True, upload_to='users_media'),
        ),
    ]
