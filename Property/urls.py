from django.urls import path
from . import views


app_name = "property"
urlpatterns = [
    path("", views.index, name="index"),
    path("browselistings", views.browselistings, name="browselistings"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("mylistings", views.mylistings, name="mylistings"),
    path("editlisting/<address1>", views.editlisting, name="editlisting"),
    path(
        "editlistingsubmit/<address1>",
        views.editlistingsubmit,
        name="editlistingsubmit",
    ),
    path("<address1>", views.propertypage, name="propertypage"),
    path("filter/<borough>", views.filter, name="filter"),
]
