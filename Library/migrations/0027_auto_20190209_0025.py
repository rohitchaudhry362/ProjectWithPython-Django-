# Generated by Django 2.1.3 on 2019-02-09 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0026_auto_20190209_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcart',
            name='BookId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book'),
        ),
    ]
