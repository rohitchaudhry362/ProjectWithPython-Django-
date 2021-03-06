# Generated by Django 2.1.3 on 2019-01-12 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0024_libraryorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibOrderDetails',
            fields=[
                ('LODId', models.AutoField(primary_key=True, serialize=False)),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
                ('LibOrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.LibraryOrder')),
            ],
        ),
    ]
