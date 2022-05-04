from django.test import TestCase, RequestFactory
from django.urls import reverse

# from account.tests import TestAccountForms
from . import views
from django.contrib.auth.models import User
from Property.models import Listing


class TestPropertyFormsNew(TestCase):
    def setUp(self):
        self.name = "Test Property"
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
        self.bedrooms = 2
        self.bathrooms = 2
        self.area = 100
        self.rent = 100
        self.furnished = "Yes"
        self.elevator = "No"
        self.heating = "Yes"
        self.parking = "No"
        self.laundry = "Yes"
        self.matterport_link = ""
        self.photo_url = ""
        self.photo_url2 = ""
        self.photo_url3 = ""
        self.description = "The best property!"
        self.user = User.objects.create_user(
            first_name="Firstname",
            last_name="Lastname",
            username="testuser",
            password="12345",
            email="test@test.com",
        )
        self.client.login(username="testuser", password="12345")

    def testNewlistingFail(self):
        response = self.client.post(
            reverse("property:newlisting"),
            data={
                "name": self.name,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testNewListingPass(self):
        response = self.client.post(
            reverse("property:newlisting"),
            data={
                "name": self.name,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "photo_url": self.photo_url,
                "photo_url3": self.photo_url,
                "photo_url2": self.photo_url,
                "matterport_link": self.matterport_link,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testNewListingGETBlank(self):
        response = self.client.get(
            reverse("property:newlisting"),
            data={
                "name": self.name,
                "address1": self.address1,
                "address2": self.address2,
                "borough": self.borough,
                "zipcode": self.zipcode,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "photo_url": self.photo_url,
                "photo_url3": self.photo_url,
                "photo_url2": self.photo_url,
                "matterport_link": self.matterport_link,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 200)



    # def testIndex(self):
    #     request = RequestFactory().get(path="Property/index.html")
    #     response = views.index(request)
    #     self.assertEqual(response.status_code, 200)

    def testBrowseList(self):
        request = RequestFactory().get(path="property/newlisting.html")
        response = views.browselistings(request)
        self.assertEqual(response.status_code, 200)


class TestPropertyForms(TestCase):
    def setUp(self):
        self.listName = "Test Property"
        self.listing_id = 1
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
        self.bedrooms = 2
        self.bathrooms = 2
        self.area = 100
        self.rent = 100
        self.furnished = "Yes"
        self.elevator = "No"
        self.heating = "Yes"
        self.parking = "No"
        self.laundry = "Yes"
        self.matterport_link = ""
        self.photo_url = ""
        self.photo_url2 = ""
        self.photo_url3 = ""
        self.description = "The best property!"
        self.username = "TestUser"
        self.password = "1a2b3c4d"
        self.firstname = "Firstname"
        self.lastname = "Lastname"
        self.email = "email123@email1.com"
        self.phone = "1234567890"
        self.message = "message"
        self.date = "2020-10-10"
        self.user = User.objects.create_user(
            first_name="Firstname",
            last_name="Lastname",
            username=self.username,
            password=self.password,
            email="1" + self.email,
        )
        # self.user.set_password(self.password)
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        self.property = Listing.objects.create(
            name=self.listName + "1",
            address1=self.address1,
            address2=self.address2,
            borough=self.borough,
            zipcode=self.zipcode,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            area=self.area,
            rent=self.rent,
            furnished=True,
            elevator=False,
            heating=True,
            parking=False,
            laundry=True,
            matterport_link=self.matterport_link,
            photo_url=self.photo_url,
            photo_url2=self.photo_url2,
            photo_url3=self.photo_url3,
            description=self.description,
            owner=self.user,
        )

    def testPropertyView(self):
        form_data = {
            "firstName": self.firstname,
            "lastName": self.lastname,
            "email": self.email,
            "phone": self.phone,
            "tourDate": self.date,
            "message": self.message,
            "listing_id": self.listing_id,
        }
        response = self.client.post(
            reverse("property:propertypage", args=[self.listing_id]), data=form_data
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("property:propertypage", args=[self.listing_id]), data=form_data
        )

        self.assertEqual(response.status_code, 200)

    def testEditListing(self):
        # self.client.login(username = self.username, password = self.password)
        response = self.client.post(
            reverse("property:editlistingsubmit", args=[self.property.listing_id]),
            data={
                "listing_name": self.listName + "1",
                "address1": self.address1 + "1",
                "address2": self.address2 + "1",
                "borough": self.borough,
                "zipcode": self.zipcode,
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "photo_url": self.photo_url,
                "matterport_link": self.matterport_link,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testAllFilters(self):
        form = {"filters[]": ["elevator", "parking", "verified"]}
        response = self.client.post(
            reverse("property:filter"),
            form, follow = True)
        self.assertEqual(response.status_code, 200)

    def testNoFilter(self):
        form = {"filters[]": ["furnished", "heating", "laundry"]}
        response = self.client.post(
            reverse("property:filter"),
            form, follow=True)
        self.assertEqual(response.status_code, 200)

    def testDeleteProperty(self):
        response = self.client.post(reverse("property:delete", args=[self.property.listing_id]))
        self.assertEqual(response.status_code, 302)


class TestPropertyFormsNew1(TestCase):
    def setUp(self):
        self.listName = "Test Property"
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
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
        self.description = "The best property!"
        self.username = "TestUser"
        self.password = "1a2b3c4d"
        self.user = User.objects.create_user(
            first_name="Firstname",
            last_name="Lastname",
            username=self.username + "1",
            password=self.password + "1",
            email="test@test.com",
        )
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        self.property = Listing.objects.create(
            address1=self.address1,
            address2=self.address2,
            borough=self.borough,
            zipcode=self.zipcode,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            area=self.area,
            rent=self.rent,
            furnished=False,
            elevator=True,
            heating=False,
            parking=True,
            laundry=False,
            photo_url=self.photoURL,
            matterport_link=self.vrLink,
            description=self.description,
            owner=self.user,
        )

    def testEditListing(self):
        response = self.client.post(
            reverse("property:editlistingsubmit", args=[self.property.listing_id]),
            data={
                "listing_name": self.listName+'1',
                "address1": self.address1+'1',
                "address2": self.address2+'1',
                "borough": "Brooklyn",
                "zipcode": "11201",
                "bedrooms": self.bedrooms,
                "bathrooms": self.bathrooms,
                "area": self.area,
                "rent": self.rent,
                "furnished": self.furnished,
                "elevator": self.elevator,
                "heating": self.heating,
                "parking": self.parking,
                "laundry": self.laundry,
                "photo_url": self.photoURL,
                "matterport_link": self.vrLink,
                "description": self.description,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testNewComments(self):
        response = self.client.post(
            reverse("property:newrating", args=[self.property.listing_id]),
            data={"rating_value": 4},
        )
        self.assertEqual(response.status_code, 302)


class TestNewRating(TestCase):
    def setUp(self):
        self.listName = "Test Property"
        self.address1 = "Test Address 1"
        self.address2 = "Test Address 2"
        self.borough = "Manhattan"
        self.zipcode = "00000"
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
        self.description = "The best property!"
        self.username = "TestUser"
        self.password = "1a2b3c4d"
        self.user = User.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.save()
        self.user1 = User.objects.create(username=self.username + "1")
        self.user1.set_password(self.password)
        self.user1.save()
        self.client.login(username=self.username + "1", password=self.password)
        self.property = Listing.objects.create(
            address1=self.address1,
            address2=self.address2,
            borough=self.borough,
            zipcode=self.zipcode,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            area=self.area,
            rent=self.rent,
            furnished=False,
            elevator=True,
            heating=False,
            parking=True,
            laundry=False,
            photo_url=self.photoURL,
            matterport_link=self.vrLink,
            description=self.description,
            owner=self.user,
        )

    def testNewComment(self):
        response = self.client.post(
            reverse("property:newcomment", args=[self.property.listing_id]),
            data={"text": "Test comment"},
        )
        self.assertEqual(response.status_code, 302)

    def testCommentview(self):
        response = self.client.get(
            reverse("property:comment", args=[self.property.listing_id]),
        )
        self.assertEqual(response.status_code, 200)

    def testNewRating(self):
        response = self.client.post(
            reverse("property:newrating", args=[self.property.listing_id]),
            data={"rating_value": 4},
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.post(
            reverse("property:newrating", args=[self.property.listing_id]),
            data={"rating_value": 3},
        )
        self.assertEqual(response.status_code, 302)

    def testDeleteListingError(self):
        response = self.client.post(reverse("property:delete", args=[self.property.listing_id]))
        self.assertEqual(response.status_code, 302)


class TestCharts(TestCase):
    def testBronx(self):
        response = self.client.get(
            reverse("property:charts", args=["Bronx"]),
        )
        self.assertEqual(response.status_code, 200)

    def testManhattan(self):
        response = self.client.get(
            reverse("property:charts", args=["Manhattan"]),
        )
        self.assertEqual(response.status_code, 200)

    def testBrooklyn(self):
        response = self.client.get(
            reverse("property:charts", args=["Brooklyn"]),
        )
        self.assertEqual(response.status_code, 200)

    def testQueens(self):
        response = self.client.get(
            reverse("property:charts", args=["Queens"]),
        )
        self.assertEqual(response.status_code, 200)

    def testStaten(self):
        response = self.client.get(
            reverse("property:charts", args=["Staten Island"]),
        )
        self.assertEqual(response.status_code, 200)
