from datetime import datetime
from django import forms

from localflavor.us.forms import USZipCodeField
from .models import Listing, RequestTour, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, ButtonHolder, Submit, Row, Column
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            "Image size should not exceed 3 MiB. Please upload a smaller photo."
        )
    else:
        return value


class ListingForm(forms.ModelForm):
    # BOROUGHS = (
    #     ("Brooklyn", "Brooklyn"),
    #     ("Manhattan", "Manhattan"),
    #     ("Queens", "Queens"),
    #     ("Staten Island", "Staten Island"),
    #     ("Bronx", "Bronx"),
    # )

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Property Name"}),
    )
    address1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"id": "address1", "class": "hidden-el"}),
    )
    address2 = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"id": "address2", "class": "hidden-el"}),
    )
    borough = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"id": "borough", "class": "hidden-el"}),
    )
    zipcode = USZipCodeField(
        required=True,
        widget=forms.TextInput(attrs={"id": "zipcode", "class": "hidden-el"}),
    )
    longitude = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"id": "longitude", "class": "hidden-el"}),
    )
    latitude = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"id": "latitude", "class": "hidden-el"}),
    )
    rent = forms.IntegerField(min_value=1, max_value=50000, required=True)
    area = forms.IntegerField(min_value=1, max_value=100000, required=True)
    bedrooms = forms.IntegerField(min_value=1, max_value=15, required=True)
    bathrooms = forms.DecimalField(
        min_value=1, max_value=10, decimal_places=2, required=True
    )
    furnished = forms.BooleanField(required=False)
    laundry = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    photo_url = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Upload Primary Photo",
        required=False,
    )
    photo_url2 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Upload Second Photo",
        required=False,
    )
    photo_url3 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        validators=[file_size],
        label="Upload Third Photo",
        required=False,
    )
    description = forms.CharField(
        required=False,
        max_length=300,
        widget=forms.Textarea(attrs={"rows": 4, "cols": 40}),
    )
    matterport_link = forms.URLField(label="Matterport Link", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("address1", css_class="form-group col-md-8 mb-0 disabled"),
                Column("address2", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("borough", css_class="form-group col-md-6 mb-0"),
                Column("zipcode", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("longitude", css_class="form-group col-md-6 mb-0"),
                Column("latitude", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "name",
            Row(
                Column("rent", css_class="form-group col-md-6 mb-0"),
                Column("area", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("bedrooms", css_class="form-group col-md-6 mb-0"),
                Column("bathrooms", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("furnished", css_class="form-group col-md-2 mb-0"),
                Column("laundry", css_class="form-group col-md-2 mb-0"),
                Column("heating", css_class="form-group col-md-2 mb-0"),
                Column("elevator", css_class="form-group col-md-2 mb-0"),
                Column("parking", css_class="form-group col-md-2 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("photo_url", css_class="form-group col-md-4 mb-0"),
                Column("photo_url2", css_class="form-group col-md-4 mb-0"),
                Column("photo_url3", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            "matterport_link",
            "description",
            ButtonHolder(
                Submit("submit", "Submit", css_class="btn btn-primary"),
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
            "longitude",
            "latitude",
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
                initial=self.user.profile.phone if self.user.is_authenticated else "",
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


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        max_length=100,
        required=False,
        label="Review and Comments",
        widget=forms.TextInput(attrs={"placeholder": "Add your review/comment here"}),
    )
    # listing = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Comment
        fields = [
            "text",
        ]
