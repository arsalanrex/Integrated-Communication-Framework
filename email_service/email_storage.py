# email_service/email_storage.py

import aiosqlite
from config.settings import DATABASE_URI

class EmailStorage:
    async def store_email(self, sender, recipient, subject, body):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                INSERT INTO emails (sender, recipient, subject, body, read, timestamp)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            ''', (sender, recipient, subject, body, False))
            await db.commit()

    async def get_emails(self, user):
        async with aiosqlite.connect(DATABASE_URI) as db:
            async with db.execute('''
                SELECT id, sender, subject, body, read, timestamp
                FROM emails
                WHERE recipient = ?
                ORDER BY timestamp DESC
            ''', (user,)) as cursor:
                emails = await cursor.fetchall()
                return [
                    {
                        "id": email[0],
                        "sender": email[1],
                        "subject": email[2],
                        "body": email[3],
                        "read": bool(email[4]),
                        "timestamp": email[5]
                    }
                    for email in emails
                ]

    async def mark_as_read(self, user, email_id):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                UPDATE emails
                SET read = TRUE
                WHERE id = ? AND recipient = ?
            ''', (email_id, user))
            await db.commit()
            return True

    async def delete_email(self, user, email_id):
        async with aiosqlite.connect(DATABASE_URI) as db:
            await db.execute('''
                DELETE FROM emails
                WHERE id = ? AND recipient = ?
            ''', (email_id, user))
            await db.commit()
            return True