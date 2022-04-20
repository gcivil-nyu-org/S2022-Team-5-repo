from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Comment, Rating
from account.models import UserProfile
from .forms import ListingForm, RequestTourForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail  # , BadHeaderError
from django.conf import settings

from django.db.models import Avg
# TODO validate email
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


def index(request):
    return render(request, "property/index.html")


def browselistings(request):
    listings = Listing.objects.all().order_by("rent")
    return render(request, "property/browselistings.html", {"listings": listings})


def newlisting(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ListingForm(request.POST, request.FILES or None)
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
            result = "Success"
            message = "Your profile has been updated"

        else:
            print(form.errors)
            result = "Failed"
            message = "Failed to save listings form"
            data = {"result": result, "message": message}
            print(data)
            messages.error(request, form.errors)
            return redirect(reverse("property:newlisting"))
        return redirect(reverse("property:mylistings"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListingForm()
        context = {"form": form}
    return render(request, "property/newlisting.html", context)


@login_required(login_url="/account/loginform")
def mylistings(request):
    user_listings = Listing.objects.filter(owner=request.user)
    return render(request, "property/mylistings.html", {"listings": user_listings})


def propertypage(request, address1):
    if request.method == "POST":
        listing = Listing.objects.get(address1=address1)
        form = RequestTourForm(
            request.POST, request.FILES or None, user=request.user, listing=listing
        )
        if form.is_valid():
            obj = form.save(commit=False)
            if request.user.is_authenticated:
                obj.requester = UserProfile.objects.get(username=request.user.username)
            obj.listing = listing
            obj.firstName = (
                request.POST.get("firstName")
                if request.POST.get("firstName")
                else form["firstName"].value()
            )
            obj.lastName = (
                request.POST.get("lastName")
                if request.POST.get("lastName")
                else form["lastName"].value()
            )
            obj.email = (
                request.POST.get("email")
                if request.POST.get("email")
                else form["email"].value()
            )
            obj.phone = (
                request.POST.get("phone")
                if request.POST.get("phone")
                else form["phone"].value()
            )
            obj.message = request.POST.get("message")
            obj.tourDate = request.POST.get("tourDate")

            obj.save()
            message = (
                obj.message
                + "\n\n"
                + "Contact details of the user:"
                + "\n"
                + obj.firstName
                + " "
                + obj.lastName
                + "\n"
                + obj.email
                + "\n"
                + obj.phone
                + "\n"
                + "Tour date requested:"
                + " "
                + obj.tourDate
            )
        send_mail(
            subject="A User has requested to view your property",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[listing.owner.email],
            fail_silently=False,
        )

        successMessage = "You have successfully requested a tour!"
        messages.success(request, successMessage)
        property_id = listing.listing_id
        comments = Comment.objects.filter(listing=property_id)
        print("Comments", comments)
        comment_form = CommentForm()
        listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
        context = context = {"listing": listing, "successMessage": successMessage, "form": form, "comments": comments, "property_id": property_id, "listing_rating": listing_rating, "comment_form": comment_form}
        return render(request, "property/property_page.html", context)
    else:
        listing = Listing.objects.get(address1=address1)
        form = RequestTourForm(user=request.user, listing=listing)
        property_id = listing.listing_id
        comments = Comment.objects.filter(listing=property_id)
        print("Comments", comments)
        comment_form = CommentForm()
        listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
        context = {"listing": listing, "form": form, "comments": comments, "property_id": property_id, "listing_rating": listing_rating, "comment_form": comment_form}
        return render(request, "property/property_page.html", context)


def filter(request, borough):
    listings = Listing.objects.filter(borough=borough)
    return render(request, "property/browselistings.html", {"listings": listings})


@login_required(login_url="/account/loginform")
def comment(request, property_id):
    # property_id = 1
    comments = Comment.objects.filter(listing=property_id)
    comment_form = CommentForm()
    listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
    print("listing_rating", listing_rating)
    return render(request, "property/comments.html", {"comments": comments, "property_id": property_id, "comment_form": comment_form, "listing_rating": listing_rating})


@login_required(login_url="/account/loginform")
def newcomment(request, property_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save()
            if request.user is not None:
                user = request.user
                obj.user = user
                listing = Listing.objects.filter(listing_id=property_id)[0]
                obj.listing = listing
                obj.save()
                address1 = listing.address1
                print(address1)
    return redirect(reverse("property:propertypage", kwargs={'address1': address1}))


@login_required(login_url="/account/loginform")
def editlisting(request, address1):
    listing = get_object_or_404(Listing, address1=address1)
    if request.user != listing.owner:
        return HttpResponseRedirect("../browselistings")
    else:
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


@login_required(login_url="/account/loginform")
def newrating(request, property_id):
    if request.method == "POST":
        rating = request.POST['rating_value']
        print(rating)
        user = request.user
        listing = Listing.objects.filter(listing_id=property_id)[0]
        print(listing)
        print('listing ', listing)
        existing_rating = Rating.objects.filter(user=user, listing=listing)
        print("ratings ", existing_rating)
        if len(existing_rating) > 0:
            t = existing_rating[0]
            t.value = rating
        else:
            t = Rating(listing=listing, user=user, value=rating)
        print(t)
        print(t.value)
        t.save()
        listing_rating = Rating.objects.filter(listing=listing)
        listing_avg = listing_rating.aggregate(Avg('value'))
        listing.ratings = listing_avg['value__avg']
        listing.save()
        address1 = listing.address1
        print(listing_rating)
        print("listing average", listing_avg['value__avg'])
    return redirect(reverse("property:propertypage", kwargs={'address1': address1}))
