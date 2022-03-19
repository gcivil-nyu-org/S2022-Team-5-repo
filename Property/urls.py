from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("createlistingform", views.createlistingform, name="createlistingform"),
    path("browselistings", views.browselistings, name="browselistings"),
]
