# Generated by Django 2.1.3 on 2019-02-11 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Librarian', '0003_stream1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(default='MYBOOK', max_length=100)),
                ('Price', models.IntegerField(default=50)),
                ('Edition', models.IntegerField(blank=True, null=True)),
                ('CoverPageImg', models.ImageField(blank=True, null=True, upload_to='Library_media')),
                ('BookSerialNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('PublishingYear', models.DateTimeField(auto_now_add=True)),
                ('BookAuthorName', models.CharField(blank=True, default=True, max_length=100)),
                ('BookCatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Librarian.BookCategory1')),
                ('StreamId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Librarian.Stream1')),
            ],
        ),
    ]