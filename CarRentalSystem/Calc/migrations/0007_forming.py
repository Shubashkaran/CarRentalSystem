# Generated by Django 3.0.3 on 2020-06-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calc', '0006_auto_20200607_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('pdate', models.DateField()),
                ('ddate', models.DateField()),
                ('passa', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]