from django.contrib import admin
from .models import Listing, RequestTour

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "name",
        "address1",
        "address2",
        "zipcode",
        "latitude",
        "longitude",
        "description",
        "rent",
        "bedrooms",
        "furnished",
        "elevator",
        "heating",
        "ratings",
        "bathrooms",
        "active",
    ]
    list_filter = [
        "created_at",
        "ratings",
        "bathrooms",
        "active",
        "bedrooms",
    ]


class RequestTourAdmin(admin.ModelAdmin):
    list_display = [
        "requester",
        "listing",
        "firstName",
        "lastName",
        "email",
        "phone",
        "message",
        "tourDate",
    ]
    list_filter = [
        "requester",
        "listing",
        "firstName",
        "lastName",
        "email",
        "phone",
        "message",
        "tourDate",
    ]


admin.site.register(Listing, ListingAdmin)
admin.site.register(RequestTour, RequestTourAdmin)
admin.site.site_header = "HouseMe Admin"
admin.site.site_title = "HouseMe Admin"
admin.site.index_title = "HouseMe Admin"
