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
        """
        A get request on signup form
        """
        response = self.client.post(reverse("account:signupform"))
        self.assertEqual(response.status_code, 200)
    
    