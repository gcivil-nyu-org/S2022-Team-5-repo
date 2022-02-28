from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('properties/', views.properties),
    path('user/', views.user),
    path('login/', views.login),
    path('register/', views.register),
]