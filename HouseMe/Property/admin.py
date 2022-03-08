from django.contrib import admin
from .models import *
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display=['city_id', 'created_at', 'name', 'state']

class StateAdmin(admin.ModelAdmin):
    list_display=['state_id', 'created_at', 'name']

class ListingAdmin(admin.ModelAdmin):
    list_display=['listing_id', 'created_at', 'name', 'address1', 'address2', 'city', 'state', 'zipcode', 'latitude', 'longitude', 'description', 'rent', 'bedrooms', 'furnished', 'elevator', 'heating', 'ratings', 'bathroom', 'active']
    list_filter=['created_at','zipcode', 'ratings', 'bathroom', 'active', 'bedrooms', 'city', 'state']


admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.site_header = "HouseMe Admin"
admin.site.site_title = "HouseMe Admin"
admin.site.index_title = "HouseMe Admin"
