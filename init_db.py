# init_db.py
import aiosqlite
import os

DATABASE_URI = os.getenv('DATABASE_URI', 'integrated_communication.db')

async def init_db():
    async with aiosqlite.connect(DATABASE_URI) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                sender TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

if __name__ == '__main__':
    import asyncio
    asyncio.run(init_db())