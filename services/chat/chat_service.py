# services/chat/chat_service.py

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_manager import get_db
from utils.helpers import generate_unique_id
from sqlalchemy import text

class ChatService:
    async def send_message(self, db: AsyncSession, sender: str, recipient: str, content: str):
        message_id = generate_unique_id()
        new_message = {
            "id": message_id,
            "sender": sender,
            "recipient": recipient,
            "content": content,
            "status": "sent"
        }
        query = text(
            "INSERT INTO messages (id, sender, recipient, content, status) "
            "VALUES (:id, :sender, :recipient, :content, :status)"
        )
        try:
            await db.execute(query, new_message)
            await db.commit()
            return message_id
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")

    async def get_message(self, db: AsyncSession, message_id: str):
        query = text("SELECT * FROM messages WHERE id = :id")
        result = await db.execute(query, {"id": message_id})
        message = result.fetchone()
        if message is None:
            raise HTTPException(status_code=404, detail="Message not found")
        return dict(message)

chat_service = ChatService()