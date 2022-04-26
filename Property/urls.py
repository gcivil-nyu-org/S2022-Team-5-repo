from django.urls import path
from . import views


app_name = "property"
urlpatterns = [
    path("", views.index, name="index"),
    path("browselistings", views.browselistings, name="browselistings"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("mylistings", views.mylistings, name="mylistings"),
    path("editlisting/<int:listing_id>", views.editlisting, name="editlisting"),
    path(
        "editlistingsubmit/<listing_id>",
        views.editlistingsubmit,
        name="editlistingsubmit",
    ),
    path("<int:listing_id>", views.propertypage, name="propertypage"),
    path("filter/borough/<borough>", views.filterborough, name="filterborough"),
    path("filter", views.filter, name="filter"),
    path("comment/<int:property_id>", views.comment, name="comment"),
    path("newcomment/<int:property_id>", views.newcomment, name="newcomment"),
    path("newrating/<int:property_id>", views.newrating, name="newrating"),
    path("delete/<int:listing_id>", views.delete_post, name="delete"),
    path("charts/<borough>", views.charts, name='charts'),

]
