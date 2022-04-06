from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    uaddr = models.CharField(max_length=100, default="")
    zip = models.CharField(max_length=5, default=00000)
    phone = models.CharField(max_length=10, default="0000000000")
    created_at = models.DateTimeField(auto_now_add=True)
    renter = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email
