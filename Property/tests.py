from django.test import TestCase, RequestFactory
from django.urls import reverse

# from Property.models import User
# from account.tests import TestAccountForms
from . import views


class TestPropertyForms(TestCase):
    def setUp(self):
        self.listName = "Test Property"
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
        self.latitude = 100
        self.longitude = 100
        self.bedrooms = 2
        self.bathrooms = 2
        self.area = 100
        self.rent = 100
        self.furnished = "Yes"
        self.elevator = "No"
        self.heating = "Yes"
        self.parking = "No"
        self.laundry = "Yes"
        self.mapURL = ""
        self.photoURL = ""
        self.vrLink = ""
        self.calendlyLink = ""
        self.description = "The best property!"
        self.owner = "MinecraftSteve"

    def testCreateListing(self):
        response = self.client.post(
            reverse("property:createlisting"),
            data={
                "listing_name": self.listName,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "map_url": self.mapURL,
                "photo_url": self.photoURL,
                "matterport_link": self.vrLink,
                "calendly_link": self.calendlyLink,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 302)


class TestPropertyFormsNew(TestCase):
    def setUp(self):
        self.listName = "Test Property"
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
        self.latitude = 100
        self.longitude = 100
        self.bedrooms = 2
        self.bathrooms = 2
        self.area = 100
        self.rent = 100
        self.furnished = "No"
        self.elevator = "Yes"
        self.heating = "No"
        self.parking = "Yes"
        self.laundry = "No"
        self.mapURL = ""
        self.photoURL = ""
        self.vrLink = ""
        self.calendlyLink = ""
        self.description = "The best property!"
        self.owner = "MinecraftSteve"

    def testCreateListing(self):
        response = self.client.post(
            reverse("property:createlisting"),
            data={
                "listing_name": self.listName,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "map_url": self.mapURL,
                "photo_url": self.photoURL,
                "matterport_link": self.vrLink,
                "calendly_link": self.calendlyLink,
                "description": self.description,
                "owner": self.owner,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testEditListing(self):
        response = self.client.post(
            reverse("property:editlisting", args=[1]),
            data={
                "listing_name": self.listName,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "map_url": self.mapURL,
                "photo_url": self.photoURL,
                "matterport_link": self.vrLink,
                "calendly_link": self.calendlyLink,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testIndex(self):
        request = RequestFactory().get(path="Property/index.html")
        response = views.index(request)
        self.assertEqual(response.status_code, 200)

    # def testCreate(self):
    #     request = RequestFactory().get(path="Property/createlistingform.html")
    #     response = views.createlistingform(request)
    #     self.assertEqual(response.status_code, 200)

    def testBrowseList(self):
        request = RequestFactory().get(path="Property/createlistingform.html")
        response = views.browselistings(request)
        self.assertEqual(response.status_code, 200)

    def testProperty(self):
        request = RequestFactory().get(path="Property/createlistingform.html")
        response = views.testproperty(request)
        self.assertEqual(response.status_code, 200)
