from django.contrib import admin
from .models import Listing, Comment, Rating, RequestTour

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "name",
        "listing_id",
        "address1",
        "address2",
        "zipcode",
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
        "listing_id",
        "ratings",
        "bathrooms",
        "active",
        "bedrooms",
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["listing", "user", "text"]
    list_filter = ["listing", "user"]


class RatingAdmin(admin.ModelAdmin):
    list_display = ["listing", "user", "value"]
    list_filter = ["listing", "user", "value"]


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
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RequestTour, RequestTourAdmin)
admin.site.site_header = "HouseMe Admin"
admin.site.site_title = "HouseMe Admin"
admin.site.index_title = "HouseMe Admin"
