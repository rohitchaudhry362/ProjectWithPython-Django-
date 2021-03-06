# Generated by Django 2.1.3 on 2018-12-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_auto_20181229_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='BookAuthorName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='BookName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='BookSerialNumber',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='PublishingYear',
            field=models.DateTimeField(null=True),
        ),
    ]
