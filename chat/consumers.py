import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from account.models import UserProfile
from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, e):
        print("connected", e)
        user = self.scope["user"]
        chat_room = f"user_chatroom_{user.username}"
        self.chat_room = chat_room

        await self.channel_layer.group_add(chat_room, self.channel_name)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, e):
        print("received", e)
        received_data = json.loads(e["text"])
        message = received_data.get("message")
        sent_by_username = received_data.get("sent_by")
        send_to_username = received_data.get("send_to")
        thread_id = received_data.get("thread_id")

        if not message:
            print("Error: empty message")
            return False

        sent_by_user = await self.get_user_object(sent_by_username)
        send_to_user = await self.get_user_object(send_to_username)
        thread_obj = await self.get_thread(thread_id)

        if not sent_by_user:
            print("Error: sent by user is incorrect")
        if not send_to_user:
            print("Error: send to user is incorrect")
        if not thread_obj:
            print("Error: thread id is incorrect")

        await self.create_chat_message(thread_obj, sent_by_user, message)

        other_user_chatroom = f"user_chatroom_{send_to_username}"
        self_user = self.scope["user"]

        response = {
            "message": message,
            "sent_by": self_user.username,
            "thread_id": thread_id,
        }

        await self.channel_layer.group_send(
            other_user_chatroom, {"type": "chat_message", "text": json.dumps(response)}
        )

        await self.channel_layer.group_send(
            self.chat_room, {"type": "chat_message", "text": json.dumps(response)}
        )

    async def websocket_disconnect(self, e):
        print("disconnected", e)

    async def chat_message(self, e):
        print("chat_message", e)
        await self.send({"type": "websocket.send", "text": e["text"]})

    @database_sync_to_async
    def get_user_object(self, username):
        qs = UserProfile.objects.filter(username=username)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None

        return obj

    @database_sync_to_async
    def get_thread(self, thread_id):
        qs = Thread.objects.filter(id=thread_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None

        return obj

    @database_sync_to_async
    def create_chat_message(self, thread, user, message):
        ChatMessage.objects.create(thread=thread, user=user, message=message)
