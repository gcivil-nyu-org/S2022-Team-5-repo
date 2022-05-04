from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestAccountForms(TestCase):
    def setUp(self):
        self.firstName = "Steve"
        self.lastName = "None"
        self.username = "MinecraftSteve"
        self.phone = 9492345678
        self.password = "removedHerobrine"
        self.email = "steve@minecraft.realm"
        self.user = User.objects.create_user(
            first_name=self.firstName,
            last_name=self.lastName,
            username=self.username + "1",
            password=self.password + "1",
            email="1" + self.email,
        )
        self.user.save()

    # def testRegisterPage(self):
    #     """
    #     A get request on signup form
    #     """
    #     response = self.client.post(reverse("register"))
    #     print(response)
    #     self.assertEqual(response.status_code, 200)

    def testRegisterPage(self):
        response = self.client.post(
            reverse("register"),
            data={
                "first_name": self.firstName,
                "last_name": self.lastName,
                "username": self.username,
                "email": self.email,
                "phone_number": self.phone,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.status_code, 302)

    # def testSignupFail(self):
    #     response = self.client.post(
    #         reverse("account:signupsubmit"),
    #         data={
    #             "fname": self.firstName,
    #             "lname": self.lastName,
    #             "username": self.username,
    #             "email": self.email,
    #             "phone": self.phone,
    #             "password": self.password,
    #             "password2": self.password,
    #         },
    #     )
    #     self.assertEqual(response.status_code, 200)

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

    def testProfile(self):
        user = User.objects.create_user(
            first_name="Firstname",
            last_name="Lastname",
            username=self.username + '2',
            email="2" + self.email,
        )
        user.set_password(self.password + '2')
        user.save()
        self.client.login(username=self.username + '2', password=self.password + '2')
        response = self.client.post(
            reverse("profile"),
            data={
                "first_name": self.firstName,
                "last_name": self.lastName,
                "username": self.username+'3',
                "email": '3'+self.email,
            },
        )
        self.assertEqual(response.status_code, 302)

    def testProfile2(self):
        response = self.client.post(
            reverse("profile"),
            data={
                "phone":self.phone,
            },
        )
        self.assertEqual(response.status_code, 302)




