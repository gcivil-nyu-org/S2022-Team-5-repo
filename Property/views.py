from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Create your views here.
def index(request):
    return render(request, 'Property/index.html')

def signupform(request):
    return render(request, 'Property/signupform.html')

def signupsubmit(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    user = UserOfApp.objects.create_user(first_name = first_name, last_name = last_name, username = username, phone = phone, password = password, email=email)
    user.save()
    send_mail(
    'Email Confirmation!',
    'Congratulations! Your email ID has been authenticated. You can now go back to the login page.',
    'HouseMe Team <binvantbajwa@gmail.com>',
    [email],
    fail_silently=False,
    )
    return render(request, 'Property/loginform.html')

def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        print("Enter a valid email")
        return False

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
        return render(request, 'Property/loginform.html')

def createlistingform(request):
    payload = {
        'states': State.objects.all(),
        'cities': City.objects.all()
        }
    return render(request, 'Property/createlistingform.html', payload)

def createlisting(request):
    pass

def browselistings(request):
    listings = Listing.objects.all()
    return render(request, 'Property/browselistings.html', {'listings': listings})
