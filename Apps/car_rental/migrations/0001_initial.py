# Generated by Django 5.0.6 on 2024-06-18 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('plaque', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('weekly_fee', models.FloatField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.client')),
            ],
        ),
    ]