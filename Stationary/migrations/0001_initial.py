# Generated by Django 2.1.3 on 2018-12-08 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scategory',
            fields=[
                ('CatId', models.AutoField(primary_key=True, serialize=False)),
                ('CatName', models.CharField(max_length=100)),
                ('CatImg', models.ImageField(blank=True, null=True, upload_to='Scategory_media')),
            ],
        ),
        migrations.CreateModel(
            name='Sproduct',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False)),
                ('PName', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('PImg', models.ImageField(blank=True, null=True, upload_to='Sproduct_media')),
                ('CatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stationary.Scategory')),
            ],
            options={
                'get_latest_by': 'Pid',
            },
        ),
    ]
