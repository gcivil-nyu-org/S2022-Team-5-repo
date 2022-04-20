from django.urls import path
from . import views


app_name = "property"
urlpatterns = [
    path("", views.index, name="index"),
    path("browselistings", views.browselistings, name="browselistings"),
    # TODO: use slug so new properties that are registered can be dynamically added
    # path("<slug>", views.),
    path("newlisting", views.newlisting, name="newlisting"),
    path("mylistings", views.mylistings, name="mylistings"),
    path("editlisting/<int:listing_id>", views.editlisting, name="editlisting"),
    path(
        "editlistingsubmit/<int:listing_id>",
        views.editlistingsubmit,
        name="editlistingsubmit",
    ),
    path("<int:listing_id>", views.propertypage, name="propertypage"),
    path("filter/<borough>", views.filter, name="filter"),
    path("comment/<property_id>", views.comment, name="comment"),
    path("newcomment/<property_id>", views.newcomment, name="newcomment"),
    path("newrating/<property_id>", views.newrating, name="newrating"),

]
