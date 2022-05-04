from django.contrib import admin
from .models import Profile

# class UserAdmin(admin.ModelAdmin):
#     list_display = ["id", "created_at", "username", "first_name", "last_name", "email"]
#     search_fields = ["id", "first_name", "last_name", "email"]

admin.site.register(Profile)
