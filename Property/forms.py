from datetime import datetime

# from faulthandler import disable
from django import forms

# from localflavor.us.forms import USZipCodeField
from .validators import file_size
from .models import Listing, RequestTour
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, ButtonHolder, Submit


class ListingForm(forms.ModelForm):
    BOROUGHS = (
        (1, "Brooklyn"),
        (2, "Manhattan"),
        (3, "Queens"),
        (4, "Staten Island"),
        (5, "Bronx"),
    )

    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Property Name"}),
    )
    address1 = forms.CharField(max_length=100, required=True)
    address2 = forms.CharField(max_length=100, required=False)
    borough = forms.ChoiceField(required=True, choices=BOROUGHS)
    # zipcode = USZipCodeField()
    latitude = forms.CharField(max_length=100, required=False)
    longitude = forms.CharField(max_length=100, required=False)
    rent = forms.IntegerField(min_value=1, max_value=50000, required=True)
    area = forms.IntegerField(min_value=1, max_value=10000, required=True)
    bedrooms = forms.IntegerField(min_value=1, max_value=10, required=True)
    bathrooms = forms.DecimalField(
        min_value=1, max_value=10, decimal_places=2, required=True
    )
    furnished = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    laundry = forms.BooleanField(required=False)
    photo_url = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Upload Primary Photo",
    )
    photo_url2 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Uplaod Second Photo",
        required=False,
    )
    photo_url3 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Upload Third Photo",
        required=False,
    )
    calendly_link = forms.URLField(label="Calendly Link", required=False)
    description = forms.CharField(required=False)
    matterport_link = forms.URLField(label="Matterport Link", required=False)
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "My awesome property description"}
        ),
    )

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


class RequestTourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.listing = kwargs.pop("listing", None)
        self.user = kwargs.pop("user", None)

        super(RequestTourForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields["firstName"] = forms.CharField(
                max_length=32,
                required=True,
                label="First Name",
                widget=forms.TextInput(attrs={"placeholder": "John"}),
                initial=self.user.first_name if self.user.is_authenticated else "",
                disabled=True if self.user.is_authenticated else False,
            )
            self.fields["lastName"] = forms.CharField(
                max_length=32,
                required=True,
                label="Last Name",
                widget=forms.TextInput(attrs={"placeholder": "Doe"}),
                initial=self.user.last_name if self.user.is_authenticated else "",
                disabled=True if self.user.is_authenticated else False,
            )
            self.fields["email"] = forms.EmailField(
                required=True,
                widget=forms.EmailInput(attrs={"placeholder": "example@email.com"}),
                initial=self.user.email if self.user.is_authenticated else "",
                disabled=True if self.user.is_authenticated else False,
            )
            self.fields["phone"] = forms.CharField(
                max_length=12,
                required=False,
                widget=forms.TextInput(attrs={"placeholder": "000-000-0000"}),
                initial=self.user.phone if self.user.is_authenticated else "",
                disabled=True if self.user.is_authenticated else False,
            )
            self.fields["tourDate"] = forms.DateField(
                label="Tour Date",
                widget=forms.DateInput(
                    attrs={"type": "date", "min": datetime.now().date()}
                ),
            )
            self.fields["message"] = forms.CharField(
                max_length=500,
                required=False,
                widget=forms.Textarea(
                    attrs={
                        "placeholder": "Enter additional information you want the seller to see, e.g., preferred time."
                    }
                ),
            )
            disable = (
                True if self.user.username == self.listing.owner.username else False
            )
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Div(
                    Field("firstName", wrapper_class="col-md-3 mb-3"),
                    Field("lastName", wrapper_class="col-md-3 mb-3"),
                    css_class="form-row row",
                ),
                Div(
                    Field("email", wrapper_class="col-md-3 mb-3"),
                    Field("phone", wrapper_class="col-md-3 mb-3"),
                    Field("tourDate", wrapper_class="col-md-3 mb-3"),
                    css_class="form-row row",
                ),
                Div(Field("message"), css_class="form-row"),
                ButtonHolder(
                    Submit(
                        "submit",
                        "Request Tour",
                        css_class="btn btn-primary",
                        disabled=disable,
                    ),
                ),
            )

    class Meta:
        model = RequestTour
        fields = [
            "firstName",
            "lastName",
            "email",
            "phone",
            "tourDate",
            "message",
        ]
