from django.test import TransactionTestCase

# from django.urls import reverse
from channels.testing import WebsocketCommunicator

from django.contrib.auth.models import User
from HouseMe.asgi import application
from .models import Thread

# Create your tests here.


class TestChat(TransactionTestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            first_name="first1",
            last_name="last1",
            username="test1",
            password="1234",
            email="test1@nyu.edu",
        )
        self.user2 = User.objects.create_user(
            first_name="first2",
            last_name="last2",
            username="test2",
            password="1234",
            email="tes2t@nyu.edu",
        )

        self.client.login(username=self.user1.username, password=self.user1.password)
        self.thread = Thread(first_person=self.user1, second_person=self.user2)

    async def testConsumer(self):
        headers = [
            (b"origin", b"..."),
            (b"cookie", self.client.cookies.output(header="", sep="; ").encode()),
        ]
        communicator = WebsocketCommunicator(application, "/chat/", headers)

        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        # self.assertEquals(communicator.scope["user"], self.user1)

        await communicator.send_json_to(
            {
                "message": "hello from unit test",
                "sent_by": self.user1.username,
                "send_to": self.user2.username,
            }
        )
        response = await communicator.receive_json_from()
        self.assertTrue(response["message"] == "hello from unit test")

        await communicator.disconnect()

    def testUserThreads(self):
        threads = (
            Thread.objects.byUser(user=self.user1)
            .prefetch_related("chatmessage_thread")
            .order_by("timestamp")
        )
        print(threads)

        # response = self.client.post(reverse("chat:chatPage"), data=threads)
        # self.assertEqual(response.status_code, 200)
