# Generated by Django 2.1.3 on 2019-02-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Librarian', '0002_auto_20190211_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream1',
            fields=[
                ('StreamId', models.AutoField(primary_key=True, serialize=False)),
                ('StreamName', models.CharField(max_length=100)),
                ('BookCatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Librarian.BookCategory1')),
            ],
            options={
                'get_latest_by': 'StreamId',
            },
        ),
    ]