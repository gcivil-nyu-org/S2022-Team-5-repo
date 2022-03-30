from django.test import TestCase
from django.urls import reverse
from Property.models import UserOfApp


class TestAccountForms(TestCase):
    def setUp(self):
        self.firstName = "Steve"
        self.lastName = "None"
        self.username = "MinecraftSteve"
        self.phone = 0000000000
        self.password = "removedHerobrine"
        self.email = "steve@minecraft.realm"
        self.user = UserOfApp.objects.create_user(
            first_name=self.firstName,
            last_name=self.lastName,
            username=self.username + "1",
            phone=self.phone,
            password=self.password + "1",
            email="1" + self.email,
        )
        self.user.save()

    def testSignupForm(self):
        """
        A get request on signup form
        """
        response = self.client.post(reverse("account:signupform"))
        self.assertEqual(response.status_code, 200)

    def testSignupSubmit(self):
        response = self.client.post(
            reverse("account:signupsubmit"),
            data={
                "fname": self.firstName,
                "lname": self.lastName,
                "username": self.username,
                "email": self.email,
                "phone": self.phone,
                "password": self.password,
            },
        )
        self.assertEqual(response.status_code, 200)

    def testLoginSubmit(self):
        response = self.client.post(
            reverse("account:loginsubmit"),
            data={
                "username": self.username + "1",
                "password": self.password + "1",
            },
        )
        self.assertEqual(response.status_code, 302)

    def testPasswordResetRequest(self):
        response = self.client.post(
            reverse("account:password_reset"),
            data={
                "email": "1" + self.email,
            },
        )
        self.assertEqual(response.status_code, 302)
