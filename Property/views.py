from django.shortcuts import render
from django.contrib.auth import authenticate, login  # , logout
from .models import UserOfApp, City, State, Listing
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from django.conf import settings
# TODO validate email
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    return render(request, "property/index.html")


def createlistingform(request):
    payload = {"states": State.objects.all(), "cities": City.objects.all()}
    return render(request, "property/createlistingform.html", payload)


def createlisting(request):
    name = request.POST['listing_name']
    address1 = request.POST['address1']
    address2 = request.POST['address2']
    city = request.POST['city']
    state = request.POST['state']
    borough = request.POST['borough']
    zipcode = request.POST['zipcode']
    latitude = request.POST['latitude']
    latitude = request.POST['latitude']
    bedrooms = request.POST['bedrooms']
    bathrooms = request.POST['bathrooms']
    area = request.POST['area']
    rent = request.POST['rent']
    furnished = request.POST['furnished']
    elevator = request.POST['elevator']
    heating = request.POST['heating']
    parking = request.POST['parking']
    laundry = request.POST['laundry']
    map_url = request.POST['map_url']
    photo_url = request.POST['photo_url']
    matterport_link = request.POST['matterport_link']
    description = request.POST['description']
    owner = request.user
    city = City.objects.get(name=city)
    state = State.objects.get(name = state)



def browselistings(request):
    listings = Listing.objects.all()
    return render(request, "property/browselistings.html", {"listings": listings})


def testproperty(request):
    return render(request, "property/property_page.html")
