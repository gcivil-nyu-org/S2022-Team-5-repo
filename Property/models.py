from datetime import datetime
from django.db import models
from account.models import UserProfile

# from django.template.defaultfilters import slugify


# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    address1 = models.CharField(
        # verbose_name="Address_1", max_length=100, null=True, blank=True
        verbose_name="Address_1",
        max_length=100,
        primary_key=True,
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
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    active = models.BooleanField(default=False)
    ratings = models.FloatField(default=1, null=True, blank=True)
    # slug = models.SlugField(slugify(address1))

    def __str__(self) -> str:
        return f"owner: {self.owner} \n address:{self.address1} {self.address2}"


# class Images(models.Model):

#   listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True)
#  image = models.FileField(upload_to="media/", verbose_name='Image')
# image= S3DirectField(dest='example_destination')


class RequestTour(models.Model):
    requester = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=UserProfile,
    )
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=False, blank=False, default=Listing
    )

    firstName = models.CharField(
        verbose_name="First Name", max_length=32, null=False, blank=False, default="N/A"
    )
    lastName = models.CharField(
        verbose_name="Last Name", max_length=32, null=False, blank=False, default="N/A"
    )
    email = models.EmailField(
        verbose_name="Email", null=False, blank=False, default="N/A"
    )
    phone = models.CharField(verbose_name="Phone", max_length=12, null=True, blank=True)
    message = models.CharField(
        verbose_name="Message", max_length=500, null=True, blank=True
    )
    tourDate = models.DateField(
        verbose_name="Tour Date", null=False, blank=False, default=datetime.now
    )
