# Generated by Django 3.0.3 on 2020-04-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
    ]
