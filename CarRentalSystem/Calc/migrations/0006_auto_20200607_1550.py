# Generated by Django 3.0.3 on 2020-06-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calc', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='CDPlayer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='CrashSensor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='LeatherSeats',
            field=models.BooleanField(default=False),
        ),
    ]
