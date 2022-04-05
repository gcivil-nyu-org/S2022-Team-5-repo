from django.shortcuts import render
from .models import User, Listing
from django.http import HttpResponseRedirect
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
    photo_url = request.FILES.get("photo_url")
    matterport_link = request.POST["matterport_link"]
    calendly_link = request.POST["calendly_link"]
    description = request.POST["description"]
    try:
        owner = User.objects.filter(username=request.user.username)[0]
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
            owner=owner,
        )
        listing.save()

        return HttpResponseRedirect("browselistings")
    except IndexError:
        return HttpResponseRedirect("/account/loginform")


def browselistings(request):
    listings = Listing.objects.all()
    return render(request, "Property/browselistings.html", {"listings": listings})


def testproperty(request):
    return render(request, "Property/property_page.html")


@login_required(login_url="/account/loginform")
def mylistings(request):
    user_listings = Listing.objects.filter(owner=request.user)
    return render(request, "Property/mylistings.html", {"listings": user_listings})


@login_required(login_url="/account/loginform")
def editlisting(request, listing_id):
    listing = Listing.objects.filter(listing_id=listing_id)[0]
    return render(request, "Property/editlisting.html", {"listing": listing})


@login_required(login_url="/account/loginform")
def editlistingsubmit(request, listing_id):
    listing = Listing.objects.filter(listing_id=listing_id)[0]

    listing.name = request.POST["listing_name"]
    listing.address1 = request.POST["address1"]
    listing.address2 = request.POST["address2"]
    listing.borough = request.POST["borough"]
    listing.zipcode = request.POST["zipcode"]
    listing.latitude = request.POST["latitude"]
    listing.longitude = request.POST["longitude"]
    listing.bedrooms = request.POST["bedrooms"]
    listing.bathrooms = request.POST["bathrooms"]
    listing.area = request.POST["area"]
    listing.rent = request.POST["rent"]
    furnished = request.POST["furnished"]
    elevator = request.POST["elevator"]
    heating = request.POST["heating"]
    parking = request.POST["parking"]
    laundry = request.POST["laundry"]
    listing.map_url = request.POST["map_url"]
    listing.photo_url = request.FILES.get("photo_url")
    listing.matterport_link = request.POST["matterport_link"]
    listing.calendly_link = request.POST["calendly_link"]
    listing.description = request.POST["description"]

    if furnished == "Yes":
        listing.furnished = True
    else:
        listing.furnished = False
    if elevator == "Yes":
        listing.elevator = True
    else:
        listing.elevator = False
    if heating == "Yes":
        listing.heating = True
    else:
        listing.heating = False
    if parking == "Yes":
        listing.parking = True
    else:
        listing.parking = False
    if laundry == "Yes":
        listing.laundry = True
    else:
        listing.laundry = False

    listing.save()

    return HttpResponseRedirect("../browselistings")
