# Generated by Django 2.1.3 on 2019-02-18 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0017_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('docid', models.AutoField(primary_key=True, serialize=False)),
                ('adharcard', models.FileField(blank=True, null=True, upload_to='documents')),
                ('result10', models.FileField(blank=True, null=True, upload_to='documents')),
                ('result12', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult1', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult2', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult3', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult4', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult5', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult6', models.FileField(blank=True, null=True, upload_to='documents')),
                ('semresult7', models.FileField(blank=True, null=True, upload_to='documents')),
                ('enroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
    ]
