from django.test import TestCase, RequestFactory
from django.urls import reverse

# from Property.models import User
# from account.tests import TestAccountForms
from . import views
from account.models import UserProfile


class TestPropertyFormsNew(TestCase):
    def setUp(self):
        self.name = "Test Property"
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

        self.user = UserProfile.objects.create_user(
            first_name="test_f",
            last_name="test_l",
            username="testuser",
            phone="123455555",
            password="12345",
            email="yx2304@nyu.com",
        )
        self.client.login(username="testuser", password="12345")

    def testNewlistings(self):
        response = self.client.post(
            reverse("property:newlisting"),
            data={
                "name": self.name,
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
            },
        )
        self.assertEqual(response.status_code, 302)

    # def testIndex(self):
    #     request = RequestFactory().get(path="Property/index.html")
    #     response = views.index(request)
    #     self.assertEqual(response.status_code, 200)

    def testBrowseList(self):
        request = RequestFactory().get(path="property/newlisting.html")
        response = views.browselistings(request)
        self.assertEqual(response.status_code, 200)
