from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserOfApp(AbstractUser):
    uaddr = models.CharField(max_length=100, default="")
    zip = models.CharField(max_length=6, default=000000)
    state = models.CharField(max_length=100, default="x")
    city = models.CharField(max_length=100, default="x")
    phone = models.CharField(max_length=10, default="0000000000")
    created_at = models.DateTimeField(auto_now_add=True)
    renter = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="state",
        default=-1,
        db_column="state_id",
    )

    def __str__(self):
        return self.name


class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=100, default=-1)
    address2 = models.CharField(max_length=120, default=-1)
    borough = models.CharField(max_length=120, default=-1)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="city",
        default=-1,
        db_column="city_name",
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="class_state",
        default=-1,
        db_column="state_name",
    )
    zipcode = models.CharField(max_length=8, default=-1)
    latitude = models.CharField(max_length=300, default="")
    longitude = models.CharField(max_length=300, default="")
    rent = models.IntegerField(default=-1)
    description = models.CharField(max_length=300, default="-")
    bedrooms = models.IntegerField(default=-1)
    furnished = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    owner = models.ForeignKey(UserOfApp, on_delete=models.CASCADE, default=None)
    heating = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    ratings = models.FloatField(default=-1)
    bathrooms = models.IntegerField(default=-1)
    area = models.FloatField(default=-1)
    active = models.BooleanField(default=False)
    map_url = models.CharField(max_length=300, default="-")
    photo_url = models.CharField(max_length=300, default=-1)
    matterport_link = models.CharField(max_length=300, default=-1)
    calendly_link = models.CharField(max_length=300, default=-1)
    # def __str__(self):
    #     return self.owner.first_name + ' ' + self.owner.last_name + ', ' + '\n' + self.shopno + '\n' +self.streetname + '\n' + str(self.city) +', ' + str(self.state) + ', ' + self.zipcode
