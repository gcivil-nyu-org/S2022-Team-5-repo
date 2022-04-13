from django.db import models
from account.models import UserProfile
from s3direct.fields import S3DirectField



# Create your models here.
class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    address1 = models.CharField(
        verbose_name="Address_1", max_length=100, null=True, blank=True
    )
    address2 = models.CharField(
        verbose_name="Address_2", max_length=120, null=True, blank=True
    )
    borough = models.CharField(
        verbose_name="Borough", max_length=120, null=True, blank=True
    )
    zipcode = models.CharField(
        verbose_name="Zip Code", max_length=8, null=True, blank=True
    )
    latitude = models.CharField(
        verbose_name="Latitude", max_length=50, null=True, blank=True
    )
    longitude = models.CharField(
        verbose_name="Longitude", max_length=50, null=True, blank=True
    )
    rent = models.IntegerField(verbose_name="Rent", default=1)
    area = models.FloatField(verbose_name="Area", default=0)
    bedrooms = models.IntegerField(verbose_name="Bedrooms", default=1)
    bathrooms = models.IntegerField(verbose_name="Bathrooms", default=1)
    furnished = models.BooleanField(verbose_name="Furnished", default=False)
    elevator = models.BooleanField(verbose_name="Elevator", default=False)
    heating = models.BooleanField(verbose_name="Heating", default=False)
    parking = models.BooleanField(verbose_name="Parking", default=False)
    laundry = models.BooleanField(verbose_name="Laundry", default=False)
    matterport_link = models.URLField(
        verbose_name="Matterport_Link", max_length=300, null=True, blank=True
    )
    photo_url = models.ImageField(upload_to="media/", null=True, blank=True)
    calendly_link = models.URLField(
        verbose_name="Calendly_Link", max_length=300, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100, null=True, blank=True)
    description = models.CharField(
        verbose_name="Description", max_length=300, null=True, blank=True
    )
    active = models.BooleanField(default=False)
    ratings = models.FloatField(default=1, null=True, blank=True)

    def __str__(self) -> str:
        return f"owner: {self.owner} \n address:{self.address1} {self.address2}"


#class Images(models.Model):

 #   listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True)
  #  image = models.FileField(upload_to="media/", verbose_name='Image')
   # image= S3DirectField(dest='example_destination')
