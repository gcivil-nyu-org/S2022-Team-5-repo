from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'Property/index.html')

def signupform(request):
    return render(request, 'Property/signupform.html')

def signupsubmit(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    username = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    user = UserOfApp.objects.create_user(first_name = first_name, last_name = last_name, username = username, phone = phone, password = password)
    user.save()
    return render(request, 'Property/loginform.html')

def loginform(request):
    return render(request, 'Property/loginform.html')

def loginsubmit(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print('sucess')
        return HttpResponseRedirect('browselistings')
    else:
        return render(reques, 'Property/loginform.html')

def createlistingform(request):
    payload = {
        'states': State.objects.all(),
        'cities': City.objects.all()
        }
    return render(request, 'Property/createlistingform.html', payload)

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
    return render(request, 'Property/browselistings.html', {'listings': listings})
