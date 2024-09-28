# api/api_manager.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.email.email_service import email_service
from services.chat.chat_service import chat_service
from database.db_manager import get_db
from pydantic import BaseModel

router = APIRouter()

class EmailSchema(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str

class MessageSchema(BaseModel):
    sender: str
    recipient: str
    content: str

@router.post("/email/send")
async def send_email(email: EmailSchema, db: AsyncSession = Depends(get_db)):
    email_id = await email_service.send_email(db, email.sender, email.recipient, email.subject, email.body)
    return {"email_id": email_id}

@router.get("/email/{email_id}")
async def get_email(email_id: str, db: AsyncSession = Depends(get_db)):
    return await email_service.get_email(db, email_id)

@router.post("/chat/send")
async def send_message(message: MessageSchema, db: AsyncSession = Depends(get_db)):
    message_id = await chat_service.send_message(db, message.sender, message.recipient, message.content)
    return {"message_id": message_id}

@router.get("/chat/{message_id}")
async def get_message(message_id: str, db: AsyncSession = Depends(get_db)):
    return await chat_service.get_message(db, message_id)