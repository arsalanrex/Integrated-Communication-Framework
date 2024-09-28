# init_db.py

import asyncio
import aiosqlite
from config.settings import DATABASE_URI

async def init_db():
    async with aiosqlite.connect(DATABASE_URI) as db:
        # Create emails table
        await db.execute('''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT NOT NULL,
                recipient TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT NOT NULL,
                read BOOLEAN NOT NULL DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create chat_messages table
        await db.execute('''
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT NOT NULL,
                recipient TEXT NOT NULL,
                message TEXT NOT NULL,
                read BOOLEAN NOT NULL DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        await db.commit()

if __name__ == '__main__':
    asyncio.run(init_db())