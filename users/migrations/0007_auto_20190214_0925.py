# Generated by Django 2.1.3 on 2019-02-14 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190214_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userdata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]