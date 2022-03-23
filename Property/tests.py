from django.test import TestCase
from django.urls import reverse


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
