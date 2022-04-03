from django.test import TestCase, RequestFactory
from django.urls import reverse

# from Property.models import User
# from account.tests import TestAccountForms
from . import views
from Property.models import User, Listing


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
        self.username = "TestUser"
        self.password = "1a2b3c4d"
        self.user = User.objects.create(is_property_owner=True, username=self.username)
        self.user.set_password(self.password)
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        self.property = Listing.objects.create(
            name=self.listName + "1",
            address1=self.address1,
            address2=self.address2,
            borough=self.borough,
            zipcode=self.zipcode,
            latitude=self.latitude,
            longitude=self.longitude,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            area=self.area,
            rent=self.rent,
            furnished=True,
            elevator=False,
            heating=True,
            parking=False,
            laundry=True,
            map_url=self.mapURL,
            photo_url=self.photoURL,
            matterport_link=self.vrLink,
            calendly_link=self.calendlyLink,
            description=self.description,
            owner=self.user,
        )

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
                "owner": self.user,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testEditListing(self):
        # self.client.login(username = self.username, password = self.password)
        response = self.client.post(
            reverse("property:editlistingsubmit", args=[self.property.listing_id]),
            data={
                "listing_name": self.listName + "1",
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
        self.username = "TestUser"
        self.password = "1a2b3c4d"
        self.user = User.objects.create(is_property_owner=True, username=self.username)
        self.user.set_password(self.password)
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        self.property = Listing.objects.create(
            address1=self.address1,
            address2=self.address2,
            borough=self.borough,
            zipcode=self.zipcode,
            latitude=self.latitude,
            longitude=self.longitude,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            area=self.area,
            rent=self.rent,
            furnished=False,
            elevator=True,
            heating=False,
            parking=True,
            laundry=False,
            map_url=self.mapURL,
            photo_url=self.photoURL,
            matterport_link=self.vrLink,
            calendly_link=self.calendlyLink,
            description=self.description,
            owner=self.user,
        )

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
                "owner": self.user,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testEditListing(self):
        response = self.client.post(
            reverse("property:editlistingsubmit", args=[self.property.listing_id]),
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
