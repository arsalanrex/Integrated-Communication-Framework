# integrated_communication/chat_service/chat_manager.py

from config.settings import USERS
from chat_service.chat_storage import ChatStorage
import asyncio

chat_storage = ChatStorage()

class ChatManager:
    def __init__(self):
        self.server = USERS

    async def send_message(self, sender, recipient, message):
        try:
            await chat_storage.store_message(sender, recipient, message)
            print(f"Message sent from {sender} to {recipient}")
            return True
        except Exception as e:
            print(f"Failed to send message: {e}")
            return False

    async def get_messages(self, user1, user2):
        return await chat_storage.get_messages(user1, user2)

    async def mark_as_read(self, user, message_id):
        return await chat_storage.mark_as_read(user, message_id)

    async def delete_message(self, user, message_id):
        return await chat_storage.delete_message(user, message_id)