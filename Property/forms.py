from email.policy import default
from pickle import FALSE
from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    address1 = forms.CharField(max_length=100, required=True)
    address2 = forms.CharField(max_length=100, required=True)
    borough = forms.CharField(max_length=100, required=True)
    zipcode = forms.CharField(max_length=100, required=True)
    latitude = forms.CharField(max_length=100, required=False)
    longitude = forms.CharField(max_length=100, required=False)
    rent = forms.IntegerField(min_value=1, required=True)
    area = forms.IntegerField(min_value=1, required=True)
    bedrooms = forms.IntegerField(min_value=1, required=True)
    bathrooms = forms.IntegerField(min_value=1, required=True)
    furnished = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    laundry = forms.BooleanField(required=False)
    photo_url = forms.URLField(label="Photo Link", required=False)
    matterport_link = forms.URLField(label="matterport Link", required=False)
    calendly_link = forms.URLField(label="calendly Link", required=False)
    name = forms.CharField(max_length=100, required=False)
    description = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Listing
        fields = [
            "address1",
            "address2",
            "borough",
            "zipcode",
            "latitude",
            "longitude",
            "rent",
            "area",
            "bedrooms",
            "bathrooms",
            "furnished",
            "elevator",
            "heating",
            "parking",
            "laundry",
            "photo_url",
            "matterport_link",
            "calendly_link",
            "name",
            "description",
        ]
