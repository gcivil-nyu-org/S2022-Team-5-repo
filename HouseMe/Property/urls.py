from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("createlistingform", views.createlistingform, name="createlistingform"),
    path("browselistings", views.browselistings, name="browselistings"),
    path("loginform", views.loginform, name="loginform"),
    path("loginsubmit", views.loginsubmit, name="loginsubmit"),
    path("signupform", views.signupform, name="signupform"),
    path("signupsubmit", views.signupsubmit, name="signupsubmit"),
]
