from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'accounts/dashboard.html')

def properties(request):
    return render(request, 'accounts/properties.html')

def user(request):
    return render(request, 'accounts/user.html')

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)