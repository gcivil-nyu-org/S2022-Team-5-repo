from django.contrib import admin
from .models import UserOfApp, Listing
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "username", "first_name", "last_name", "email"]
    search_fields = ["id", "first_name", "last_name", "email"]
    

class ListingAdmin(admin.ModelAdmin):
    list_display = [
        "listing_id",
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
        "zipcode",
        "ratings",
        "bathrooms",
        "active",
        "bedrooms",
    ]


admin.site.register(UserOfApp, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.site_header = "HouseMe Admin"
admin.site.site_title = "HouseMe Admin"
admin.site.index_title = "HouseMe Admin"
