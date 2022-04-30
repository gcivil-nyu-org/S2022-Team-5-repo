from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Comment, Rating
from django.contrib.auth.models import User
from .forms import ListingForm, RequestTourForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail  # , BadHeaderError
from django.conf import settings
import plotly.express as px
import pandas as pd


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


def propertypage(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(listing_id=listing_id)
        form = RequestTourForm(
            request.POST, request.FILES or None, user=request.user, listing=listing
        )
        if form.is_valid():
            obj = form.save(commit=False)
            if request.user.is_authenticated:
                obj.requester = User.objects.get(username=request.user.username)
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
            sub = (
                "A User has requested to view your property at :"
                + " "
                + obj.listing.address1
            )
            ph = obj.phone
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
                + str(ph)
                + "\n"
                + "Tour date requested:"
                + " "
                + obj.tourDate
                + "\n\n"
                + "Thanks and Have a Great Day!"
            )
        send_mail(
            subject=sub,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[listing.owner.email],
            fail_silently=False,
        )

        successMessage = "You have successfully requested a tour!"
        messages.info(request, successMessage)
        property_id = listing.listing_id
        comments = Comment.objects.filter(listing=property_id)
        print("Comments", comments)
        comment_form = CommentForm()
        listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
        context = context = {
            "listing": listing,
            "successMessage": successMessage,
            "form": form,
            "comments": comments,
            "property_id": property_id,
            "listing_rating": listing_rating,
            "comment_form": comment_form,
        }
        return render(request, "property/property_page.html", context)
    else:
        listing = Listing.objects.get(listing_id=listing_id)
        form = RequestTourForm(user=request.user, listing=listing)
        property_id = listing.listing_id
        comments = Comment.objects.filter(listing=property_id)
        print("Comments", comments)
        comment_form = CommentForm()
        listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
        context = {
            "listing": listing,
            "form": form,
            "comments": comments,
            "property_id": property_id,
            "listing_rating": listing_rating,
            "comment_form": comment_form,
        }
        return render(request, "property/property_page.html", context)


def filterborough(request, borough):
    listings = Listing.objects.filter(borough=borough)
    return render(request, "property/browselistings.html", {"listings": listings})


def filter(request):
    filters = request.POST.getlist("filters")
    if "furnished" in filters:
        furnished = True
    else:
        furnished = False
    if "elevator" in filters:
        elevator = True
    else:
        elevator = False
    if "heating" in filters:
        heating = True
    else:
        heating = False
    if "parking" in filters:
        parking = True
    else:
        parking = False
    if "laundry" in filters:
        laundry = True
    else:
        laundry = False
    print(filters)
    listings = Listing.objects.filter(
        furnished=furnished,
        elevator=elevator,
        heating=heating,
        parking=parking,
        laundry=laundry,
    )
    return render(request, "property/browselistings.html", {"listings": listings})


@login_required(login_url="/account/loginform")
def comment(request, property_id):
    # property_id = 1
    comments = Comment.objects.filter(listing=property_id)
    comment_form = CommentForm()
    listing_rating = Listing.objects.filter(listing_id=property_id)[0].ratings
    print("listing_rating", listing_rating)
    return render(
        request,
        "property/comments.html",
        {
            "comments": comments,
            "property_id": property_id,
            "comment_form": comment_form,
            "listing_rating": listing_rating,
        },
    )


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
                listing_id = listing.listing_id
                address1 = listing.address1
                print(address1)
    return redirect(reverse("property:propertypage", kwargs={"listing_id": listing_id}))


@login_required(login_url="/account/loginform")
def editlisting(request, listing_id):
    listing = get_object_or_404(Listing, listing_id=listing_id)
    if request.user != listing.owner:
        return HttpResponseRedirect("../browselistings")
    else:
        return render(request, "property/editlisting.html", {"listing": listing})


@login_required(login_url="/account/loginform")
def editlistingsubmit(request, listing_id):
    listing = Listing.objects.filter(listing_id=listing_id)[0]
    listing.name = request.POST["listing_name"]
    listing.address1 = request.POST["address1"]
    listing.address2 = request.POST["address2"]
    listing.borough = request.POST["borough"]
    listing.zipcode = request.POST["zipcode"]
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
    listing.photo_url2 = request.FILES.get("photo_url2")
    listing.photo_url3 = request.FILES.get("photo_url3")
    listing.matterport_link = request.POST["matterport_link"]
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
    listing = Listing.objects.filter(listing_id=property_id)[0]
    if request.user != listing.owner:
        if request.method == "POST":
            rating = request.POST["rating_value"]
            print(rating)
            user = request.user
            listing = Listing.objects.filter(listing_id=property_id)[0]

            print(listing)
            print("listing ", listing)
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
            listing_avg = listing_rating.aggregate(Avg("value"))
            listing.ratings = listing_avg["value__avg"]
            listing.save()
            listing_id = listing.listing_id
            print(listing_rating)
            print("listing average", listing_avg["value__avg"])
        return redirect(
            reverse("property:propertypage", kwargs={"listing_id": listing_id})
        )
    else:
        messages.warning(request, "You cannot rate your own listing")
        listing_id = listing.listing_id
        return redirect(
            reverse("property:propertypage", kwargs={"listing_id": listing_id})
        )


@login_required(login_url="/account/loginform")
def delete_post(request, listing_id):
    listing = get_object_or_404(Listing, listing_id=listing_id)
    if request.method == "POST":
        if request.user == listing.owner:
            post_to_delete = Listing.objects.get(listing_id=listing_id)
            post_to_delete.delete()
            return HttpResponseRedirect("../mylistings")
        else:
            return HttpResponseRedirect("../browselistings")
    else:
        return HttpResponseRedirect("../browselistings")


def charts(request, borough):
    if borough == "Bronx":
        datafile1 = settings.BASE_DIR / "data" / "bronx.csv"
        df = pd.read_csv(datafile1)
        fig = px.bar(
            df,
            x="NEIGHBORHOOD",
            y="SALE PRICE",
            animation_frame="YEAR",
            animation_group="NEIGHBORHOOD",
            title="Bronx Price Trends from 2016-2021",
            color="NEIGHBORHOOD",
            range_y=[0, 2700],
            color_discrete_sequence=px.colors.qualitative.T10,
            labels={"x": "Neighbourhoods", "y": "Price (In Millions)"},
        )
        fig.update_yaxes(showgrid=True),
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(categoryorder="total descending")
        fig.update_layout(
            margin=dict(l=15, r=20, t=20, b=200),
            hovermode="x unified",
            xaxis_title=" ",
            yaxis_title="Price in Millions",
            title_font=dict(size=15, color="#a5a7ab", family="Lato, sans-serif"),
            font=dict(color="#8a8d93"),
        )
        fig["layout"]["updatemenus"][0]["pad"] = dict(r=10, t=150)
        fig["layout"]["sliders"][0]["pad"] = dict(
            r=10,
            t=150,
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
        disp = fig.to_html()
        context = {"disp": disp}
        return render(request, "property/chart.html", context)
    elif borough == "Manhattan":
        datafile1 = settings.BASE_DIR / "data" / "manhattan.csv"
        df = pd.read_csv(datafile1)
        fig = px.bar(
            df,
            x="NEIGHBORHOOD",
            y="SALE PRICE",
            animation_frame="YEAR",
            animation_group="NEIGHBORHOOD",
            title="Manhattan Price Trends from 2016-2021",
            color="NEIGHBORHOOD",
            range_y=[0, 4500],
            color_discrete_sequence=px.colors.qualitative.T10,
            labels={"x": "Neighbourhoods", "y": "Price (In Millions)"},
        )
        fig.update_yaxes(showgrid=True),
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(categoryorder="total descending")
        fig.update_layout(
            margin=dict(l=15, r=20, t=20, b=200),
            hovermode="x unified",
            xaxis_title=" ",
            yaxis_title="Price in Millions",
            title_font=dict(size=15, color="#a5a7ab", family="Lato, sans-serif"),
            font=dict(color="#8a8d93"),
        )
        fig["layout"]["updatemenus"][0]["pad"] = dict(r=10, t=150)
        fig["layout"]["sliders"][0]["pad"] = dict(
            r=10,
            t=150,
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
        disp = fig.to_html()
        context = {"disp": disp}
        return render(request, "property/chart.html", context)
    elif borough == "Brooklyn":
        datafile1 = settings.BASE_DIR / "data" / "brooklyn.csv"
        df = pd.read_csv(datafile1)
        fig = px.bar(
            df,
            x="NEIGHBORHOOD",
            y="SALE PRICE",
            animation_frame="YEAR",
            animation_group="NEIGHBORHOOD",
            title="Brooklyn Price Trends from 2016-2021",
            color="NEIGHBORHOOD",
            range_y=[0, 1800],
            color_discrete_sequence=px.colors.qualitative.T10,
            labels={"x": "Neighbourhoods", "y": "Price (In Millions)"},
        )
        fig.update_yaxes(showgrid=True),
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(categoryorder="total descending")
        fig.update_layout(
            margin=dict(l=15, r=20, t=20, b=200),
            hovermode="x unified",
            xaxis_title=" ",
            yaxis_title="Price in Millions",
            title_font=dict(size=10, color="#a5a7ab", family="Lato, sans-serif"),
            font=dict(color="#8a8d93"),
        )
        fig["layout"]["updatemenus"][0]["pad"] = dict(r=10, t=150)
        fig["layout"]["sliders"][0]["pad"] = dict(
            r=10,
            t=150,
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
        disp = fig.to_html()
        context = {"disp": disp}
        return render(request, "property/chart.html", context)
    elif borough == "Staten Island":
        datafile1 = settings.BASE_DIR / "data" / "statenisland.csv"
        df = pd.read_csv(datafile1)
        fig = px.bar(
            df,
            x="NEIGHBORHOOD",
            y="SALE PRICE",
            animation_frame="YEAR",
            animation_group="NEIGHBORHOOD",
            title="Staten Island Price Trends from 2016-2021",
            color="NEIGHBORHOOD",
            range_y=[0, 300],
            color_discrete_sequence=px.colors.qualitative.T10,
            labels={"x": "Neighbourhoods", "y": "Price (In Millions)"},
        )
        fig.update_yaxes(showgrid=True),
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(categoryorder="total descending")
        fig.update_layout(
            margin=dict(l=15, r=20, t=20, b=200),
            hovermode="x unified",
            xaxis_title=" ",
            yaxis_title="Price (In Millions)",
            title_font=dict(size=25, color="#a5a7ab", family="Lato, sans-serif"),
            font=dict(color="#8a8d93"),
        )
        fig["layout"]["updatemenus"][0]["pad"] = dict(r=10, t=150)
        fig["layout"]["sliders"][0]["pad"] = dict(
            r=10,
            t=150,
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
        disp = fig.to_html()
        context = {"disp": disp}
        return render(request, "property/chart.html", context)
    elif borough == "Queens":
        datafile1 = settings.BASE_DIR / "data" / "queens.csv"
        df = pd.read_csv(datafile1)
        fig = px.bar(
            df,
            x="NEIGHBORHOOD",
            y="SALE PRICE",
            animation_frame="YEAR",
            animation_group="NEIGHBORHOOD",
            title="Queens Price Trends from 2016-2021",
            color="NEIGHBORHOOD",
            range_y=[0, 2500],
            color_discrete_sequence=px.colors.qualitative.T10,
            labels={"x": "Neighbourhoods", "y": "Price (In Millions)"},
        )
        fig.update_yaxes(showgrid=True),
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(categoryorder="total descending")
        fig.update_layout(
            margin=dict(l=15, r=20, t=20, b=200),
            hovermode="x unified",
            xaxis_title=" ",
            yaxis_title="Price (In Millions)",
            title_font=dict(size=25, color="#a5a7ab", family="Lato, sans-serif"),
            font=dict(color="#8a8d93"),
        )
        fig["layout"]["updatemenus"][0]["pad"] = dict(r=10, t=150)
        fig["layout"]["sliders"][0]["pad"] = dict(
            r=10,
            t=150,
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
        disp = fig.to_html()
        context = {"disp": disp}
        return render(request, "property/chart.html", context)
