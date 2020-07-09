# Generated by Django 2.1.3 on 2019-02-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stationary', '0003_statorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatOrderDetails',
            fields=[
                ('SODId', models.AutoField(primary_key=True, serialize=False)),
                ('Price', models.IntegerField(default=True)),
                ('quantity', models.IntegerField()),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stationary.Sproduct')),
                ('StatOrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stationary.StatOrder')),
            ],
        ),
    ]
