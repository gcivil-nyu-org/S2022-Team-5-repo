from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

#TODO validate email 
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request, 'Property/index.html')

def signupform(request):
    return render(request, 'Property/signupform.html')

def signupsubmit(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    username = request.POST['username']
    #TODO validate email
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']

    #TODO BUG UNIQUE constraint failed: Property_userofapp.username

    user = UserOfApp.objects.create_user(first_name = first_name, last_name = last_name, username = username, phone = phone, password = password, email = email)
    user.save()
    subject = 'Welcome to House ME!'
    message = 'Congratulations! Your email ID has been authenticated. You can now go back to the login page.'
    try:
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list= [email], fail_silently=False)
    except:
        return HttpResponse('Failed to send welcome email!')
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
