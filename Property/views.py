from django.shortcuts import render
from .models import Listing
from .forms import ListingForm


# from django.contrib.auth.decorators import login_required

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
        form = ListingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save()
            if request.user is not None:
                user = request.user
                obj.owner = user
                print(f"valid user: {obj.owner} listing")
                obj.save()
            else:
                print("unknown user listing")
        listings = Listing.objects.all()
        return render(request, "property/browselistings.html", {"listings": listings})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListingForm()
        context = {"form": form}
    return render(request, "property/newlisting.html", context)
