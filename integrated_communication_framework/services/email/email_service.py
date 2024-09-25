# services/email/email_service.py

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_manager import get_db
from utils.helpers import generate_unique_id
from sqlalchemy import text

class EmailService:
    async def send_email(self, db: AsyncSession, sender: str, recipient: str, subject: str, body: str):
        email_id = generate_unique_id()
        new_email = {
            "id": email_id,
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "status": "sent"
        }
        query = text(
            "INSERT INTO emails (id, sender, recipient, subject, body, status) "
            "VALUES (:id, :sender, :recipient, :subject, :body, :status)"
        )
        await db.execute(query, new_email)
        await db.commit()
        return email_id

    async def get_email(self, db: AsyncSession, email_id: str):
        query = text("SELECT * FROM emails WHERE id = :id")
        result = await db.execute(query, {"id": email_id})
        email = result.fetchone()
        if email is None:
            raise HTTPException(status_code=404, detail="Email not found")
        return dict(email)

email_service = EmailService()