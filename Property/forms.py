from django import forms
from .models import Listing
from localflavor.us.forms import USZipCodeField
from .validators import file_size


class ListingForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    address1 = forms.CharField(max_length=100, required=True)
    address2 = forms.CharField(max_length=100, required=False)
    borough = forms.CharField(max_length=100, required=True)
    zipcode = USZipCodeField()
    latitude = forms.CharField(max_length=100, required=False)
    longitude = forms.CharField(max_length=100, required=False)
    rent = forms.IntegerField(min_value=1, max_value=50000, required=True)
    area = forms.IntegerField(min_value=1, max_value=10000, required=True)
    bedrooms = forms.IntegerField(min_value=1, max_value=10, required=True)
    bathrooms = forms.DecimalField(min_value=1, max_value=10, decimal_places=2, required=True)
    furnished = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    laundry = forms.BooleanField(required=False)
    photo_url = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), validators=[file_size], label="Upload Primary Photo"
    )
    photo_url2 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), validators=[file_size], label="Uplaod Second Photo", required=False
    )
    photo_url3 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), validators=[file_size], label="Upload Third Photo", required=False
    )
    matterport_link = forms.URLField(label="Matterport Link", required=False)
    calendly_link = forms.URLField(label="Calendly Link", required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Listing
        fields = [
            "name",
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
            "photo_url2",
            "photo_url3",
            "matterport_link",
            "calendly_link",
            "description",
        ]
