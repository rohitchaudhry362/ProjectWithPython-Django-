# Generated by Django 2.1.3 on 2018-12-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_auto_20181229_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='BookAuthorName',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='BookName',
            field=models.CharField(default='MYBOOK', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='BookSerialNumber',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Edition',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='PublishingYear',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
    ]
