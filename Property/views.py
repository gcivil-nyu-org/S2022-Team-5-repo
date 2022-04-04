from django.shortcuts import render
from .models import Listing
from django.http import HttpResponseRedirect
from .forms import ListingForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# TODO validate email
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    return render(request, "Property/index.html")


def createlistingform(request):
    payload = {}
    return render(request, "Property/createlistingform.html", payload)


def createlisting(request):
    name = request.POST["listing_name"]
    address1 = request.POST["address1"]
    address2 = request.POST["address2"]
    borough = request.POST["borough"]
    zipcode = request.POST["zipcode"]
    latitude = request.POST["latitude"]
    longitude = request.POST["longitude"]
    bedrooms = request.POST["bedrooms"]
    bathrooms = request.POST["bathrooms"]
    area = request.POST["area"]
    rent = request.POST["rent"]
    furnished = request.POST["furnished"]
    elevator = request.POST["elevator"]
    heating = request.POST["heating"]
    parking = request.POST["parking"]
    laundry = request.POST["laundry"]
    map_url = request.POST["map_url"]
    photo_url = request.POST["photo_url"]
    matterport_link = request.POST["matterport_link"]
    calendly_link = request.POST["calendly_link"]
    description = request.POST["description"]
    # owner = request.user
    if furnished == "Yes":
        furnished = True
    else:
        furnished = False
    if elevator == "Yes":
        elevator = True
    else:
        elevator = False
    if heating == "Yes":
        heating = True
    else:
        heating = False
    if parking == "Yes":
        parking = True
    else:
        parking = False
    if laundry == "Yes":
        laundry = True
    else:
        laundry = False
    listing = Listing(
        name=name,
        address1=address1,
        address2=address2,
        borough=borough,
        zipcode=zipcode,
        latitude=latitude,
        longitude=longitude,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        area=area,
        rent=rent,
        furnished=furnished,
        elevator=elevator,
        heating=heating,
        parking=parking,
        laundry=laundry,
        map_url=map_url,
        photo_url=photo_url,
        matterport_link=matterport_link,
        description=description,
        calendly_link=calendly_link,
    )
    listing.save()
    return HttpResponseRedirect("browselistings")


def browselistings(request):
    listings = Listing.objects.all()
    return render(request, "Property/browselistings.html", {"listings": listings})


def testproperty(request):
    return render(request, "Property/property_page.html")


def newlisting(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ListingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            result = "Success"
            message = "Your profile has been updated"
        else:
            result = "Failed"
            message = "Failed to save listings form"
        data = {"result": result, "message": message}
        return JsonResponse(data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListingForm()
        context = {"form": form}
    return render(request, "property/newlisting.html", context)
