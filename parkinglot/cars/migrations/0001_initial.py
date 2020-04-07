# Generated by Django 3.0.4 on 2020-04-06 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=7)),
                ('model', models.CharField(max_length=40)),
                ('manufacturing_year', models.CharField(max_length=4)),
                ('model_year', models.CharField(max_length=4)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
    ]