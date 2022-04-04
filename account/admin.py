from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "username", "first_name", "last_name", "email"]
    search_fields = ["id", "first_name", "last_name", "email"]

admin.site.register(UserProfile, UserAdmin)