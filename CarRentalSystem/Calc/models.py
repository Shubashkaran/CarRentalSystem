from datetime import timezone

from django.db import models


# Create your models here.
class Recent(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    offer = models.BooleanField(default=False)


class about(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.CharField(max_length=200)

class slideshow(models.Model):
    img = models.ImageField(upload_to='pics')
    Title = models.CharField(max_length=100)
    desc = models.TextField()

class Booking(models.Model):
    Title = models.CharField(max_length=100)
    Brand = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    FuelType = models.CharField(max_length=50)
    NoSeats = models.IntegerField()
    Powersteering = models.BooleanField(default=False)
    AC =models.BooleanField(default=False)
    BrakeAssist = models.BooleanField(default=False)
    Airbags = models.BooleanField(default=False)
    CDPlayer = models.BooleanField(default=False)
    LeatherSeats = models.BooleanField(default=False)
    CrashSensor = models.BooleanField(default=False)
    Cost_per_day = models.IntegerField()

class Forming(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    pdate = models.DateField()
    ddate = models.DateField()
    passa = models.IntegerField()
    result = models.IntegerField()

    def __str__(self):
        return self.uname