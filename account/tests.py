from django.test import TestCase
from django.urls import reverse

# import account.views

class TestAccountForms(TestCase):
    def setUp(self):
        self.firstName = "Steve"
        self.lastName = "None"
        self.username = "MinecraftSteve"
        self.phone = 0000000000
        self.password = "removedHerobrine"
        self.email = "steve@minecraft.realm"

    def testSignupForm(self):
        response = self.client.post(reverse('signupform'), data = {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "username": self.username,
            "phone": self.phone,
            "password": self.password,
            "email": self.email,
        })
        
        self.assertEqual(response.status_code, 200)