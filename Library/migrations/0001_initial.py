# Generated by Django 2.1.3 on 2018-12-25 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Edition', models.IntegerField()),
                ('CoverPageImg', models.ImageField(blank=True, null=True, upload_to='Library_media')),
                ('BookSerialNumber', models.CharField(max_length=100)),
                ('PublishingYear', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('BookAuthorId', models.AutoField(primary_key=True, serialize=False)),
                ('BookAuthorName', models.CharField(max_length=100)),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('BookCatId', models.AutoField(primary_key=True, serialize=False)),
                ('BookCatName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('BookIssueId', models.AutoField(primary_key=True, serialize=False)),
                ('DateOfIssue', models.DateTimeField(auto_now_add=True)),
                ('DateOfReturn', models.DateTimeField()),
                ('Fine', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookStock',
            fields=[
                ('BookStockId', models.AutoField(primary_key=True, serialize=False)),
                ('BookStockSerial', models.IntegerField()),
                ('Issued', models.BooleanField(default=False)),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('StreamId', models.AutoField(primary_key=True, serialize=False)),
                ('StreamName', models.CharField(max_length=100)),
                ('BookCatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.BookCategory')),
            ],
        ),
        migrations.AddField(
            model_name='bookissue',
            name='BookStockId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.BookStock'),
        ),
        migrations.AddField(
            model_name='book',
            name='BookCatId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.BookCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='StreamId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Stream'),
        ),
    ]
