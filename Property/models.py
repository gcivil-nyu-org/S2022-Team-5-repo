from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    uaddr = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=10, default="0000000000")
    uid = models.IntegerField(default=-1, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_property_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    listing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=-1)
    created_on = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=100, default=-1)
    address2 = models.CharField(max_length=120, default=-1)
    borough = models.CharField(max_length=120, default=-1)
    zipcode = models.CharField(max_length=8, default=-1)
    latitude = models.CharField(max_length=300, default="")
    longitude = models.CharField(max_length=300, default="")
    rent = models.IntegerField(default=-1)
    description = models.CharField(max_length=300, default="-")
    bedrooms = models.IntegerField(default=-1)
    furnished = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    ratings = models.FloatField(default=-1)
    bathrooms = models.IntegerField(default=-1)
    area = models.FloatField(default=-1)
    active = models.BooleanField(default=False)
    map_url = models.CharField(max_length=300, default="-")
    photo_url = models.ImageField(upload_to='media/', null=True, blank=True)
    matterport_link = models.CharField(max_length=300, default=-1)
    calendly_link = models.CharField(max_length=300, default=-1)
    
    # def __str__(self):
    #     return self.owner.first_name + ' ' + self.owner.last_name + ', ' + '\n' + self.shopno + '\n' +self.streetname + '\n' + str(self.city) +', ' + str(self.state) + ', ' + self.zipcode
