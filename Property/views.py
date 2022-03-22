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

    return render(request, "Property/index.html")


def signupform(request):

    return render(request, "Property/signupform.html")


def signupsubmit(request):

    first_name = request.POST["fname"]
    last_name = request.POST["lname"]
    username = request.POST["username"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    password = request.POST["password"]
    user = UserOfApp.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        phone=phone,
        password=password,
        email=email,
    )
    user.save()
    send_mail(subject="Welcome to House ME!", message="Congratulations! Your email ID has been authenticated. You can now go back to the login page.", from_email=settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently=False,)
    return render(request, "Property/loginform.html")


def loginform(request):

    return render(request, "Property/loginform.html")


def loginsubmit(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print("sucess")
        return HttpResponseRedirect("browselistings")
    else:
        return render(request, "Property/loginform.html")


def createlistingform(request):
    payload = {"states": State.objects.all(), "cities": City.objects.all()}
    return render(request, "Property/createlistingform.html", payload)


def createlisting(request):
    name = request.POST['listing_name']
    address1 = request.POST['address1']
    address2 = request.POST['address2']
    city = request.POST['city']
    state = request.POST['state']
    borough = request.POST['borough']
    zipcode = request.POST['zipcode']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
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
    calendly_link = request.POST['calendly_link']
    description = request.POST['description']
    owner = request.user
    city = City.objects.get(name=city)
    state = State.objects.get(name=state)
    if furnished == 'Yes':
        furnished = True
    else:
        furnished = False
    if elevator == 'Yes':
        elevator = True
    else:
        elevator = False
    if heating == 'Yes':
        heating = True
    else:
        heating = False
    if parking == 'Yes':
        parking = True
    else:
        parking = False
    if laundry == 'Yes':
        laundry = True
    else:
        laundry = False
    listing = Listing(name=name, address1=address1, address2=address2, city=city, state=state, borough=borough, zipcode=zipcode, latitude=latitude, longitude=longitude, bedrooms=bedrooms, bathrooms=bathrooms, area=area, rent=rent, furnished=furnished, elevator=elevator, heating=heating, parking=parking, laundry=laundry, map_url=map_url, photo_url=photo_url, matterport_link=matterport_link, calendly_link=calendly_link, description=description, owner=owner)
    listing.save()
    return HttpResponseRedirect('browselistings')


def browselistings(request):
    listings = Listing.objects.all()
    return render(request, "Property/browselistings.html", {"listings": listings})
