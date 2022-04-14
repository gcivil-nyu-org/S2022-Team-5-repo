from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# TODO validate email
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


def index(request):
    return render(request, "property/index.html")


def browselistings(request):
    listings = Listing.objects.all()
    return render(request, "property/browselistings.html", {"listings": listings})


def newlisting(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ListingForm(request.POST, request.FILES or None)
        files = request.FILES.getlist("photo_url")
        # check whether it's valid:
        if form.is_valid():
            obj = form.save()
            if request.user is not None:
                user = request.user
                obj.owner = user
                print(f"valid user: {obj.owner} listing")
                obj.save()
                print(files)
            else:
                print("unknown user listing")
            result = "Success"
            message = "Your profile has been updated"
        else:
            result = "Failed"
            message = "Failed to save listings form"
        data = {"result": result, "message": message}
        print(data)
        return redirect(reverse("property:mylistings"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListingForm()
        context = {"form": form}
    return render(request, "property/newlisting.html", context)


# def propertypage(request, slug=None):
#     print(slug)
#     listing = None
#     if slug:
#         listing = Listing.objects.get(slug=slug)

#     return render(request, "property/property_page.html", {"listing": listing})


def propertypage(request, address1):
    listing = Listing.objects.get(address1=address1)
    return render(request, "property/property_page.html", {"listing": listing})


@login_required(login_url="/account/loginform")
def mylistings(request):
    user_listings = Listing.objects.filter(owner=request.user)
    return render(request, "property/mylistings.html", {"listings": user_listings})


def filter(request, borough):
    listings = Listing.objects.filter(borough=borough)
    return render(request, "property/browselistings.html", {"listings": listings})


@login_required(login_url="/account/loginform")
def editlisting(request, address1):
    # listing = Listing.objects.filter(listing_id=listing_id)[0]
    listing = get_object_or_404(Listing, address1=address1)
    return render(request, "property/editlisting.html", {"listing": listing})


@login_required(login_url="/account/loginform")
def editlistingsubmit(request, address1):
    listing = Listing.objects.filter(address1=address1)[0]

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
