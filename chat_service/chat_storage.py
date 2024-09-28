# chat_service/chat_storage.py

import aiosqlite
from config.settings import DATABASE_URI

class ChatStorage:
    async def store_message(self, sender, recipient, message):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                INSERT INTO chat_messages (sender, recipient, message, read, timestamp)
                VALUES (?, ?, ?, ?, datetime('now'))
            ''', (sender, recipient, message, False))
            await db.commit()

    async def get_messages(self, user1, user2):
        async with aiosqlite.connect(DATABASE_URI) as db:
            async with db.execute('''
                SELECT id, sender, recipient, message, read, timestamp
                FROM chat_messages
                WHERE (sender = ? AND recipient = ?) OR (sender = ? AND recipient = ?)
                ORDER BY timestamp ASC
            ''', (user1, user2, user2, user1)) as cursor:
                messages = await cursor.fetchall()
                return [
                    {
                        "id": msg[0],
                        "sender": msg[1],
                        "recipient": msg[2],
                        "message": msg[3],
                        "read": bool(msg[4]),
                        "timestamp": msg[5]
                    }
                    for msg in messages
                ]

    async def mark_as_read(self, user, message_id):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                UPDATE chat_messages
                SET read = TRUE
                WHERE id = ? AND recipient = ?
            ''', (message_id, user))
            await db.commit()
            return True

    async def delete_message(self, user, message_id):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                DELETE FROM chat_messages
                WHERE id = ? AND (sender = ? OR recipient = ?)
            ''', (message_id, user, user))
            await db.commit()
            return True