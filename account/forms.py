from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        model._meta.get_field("email")._unique = True
        fields = [
            "username",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        model._meta.get_field("email")._unique = True
        fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    phone = PhoneNumberField()

    class Meta:
        model = Profile
        fields = ["phone", "image"]
