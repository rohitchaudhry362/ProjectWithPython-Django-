# Generated by Django 2.1.3 on 2018-12-30 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0008_auto_20181229_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'get_latest_by': 'BookId'},
        ),
    ]
