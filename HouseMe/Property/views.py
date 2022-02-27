from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'Property/index.html')

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
