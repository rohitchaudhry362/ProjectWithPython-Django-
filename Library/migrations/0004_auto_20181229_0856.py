# Generated by Django 2.1.3 on 2018-12-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20181228_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='BookId',
        ),
        migrations.AddField(
            model_name='book',
            name='BookAuthorName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='BookAuthor',
        ),
    ]
