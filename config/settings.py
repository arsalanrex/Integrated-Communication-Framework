# config/settings.py

import os
from dotenv import load_dotenv
import secrets
from users import USERS

load_dotenv()

EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 1025))
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', 'your_username')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password')

CHAT_SERVER = os.getenv('CHAT_SERVER', 'localhost')
CHAT_PORT = int(os.getenv('CHAT_PORT', 5222))

DATABASE_URI = os.getenv('DATABASE_URI', 'integrated_communication.db')

# Generate a proper SECRET_KEY if not provided
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = secrets.token_bytes(32)

# WebSocket settings
WEBSOCKET_HOST = os.getenv('WEBSOCKET_HOST', 'localhost')
WEBSOCKET_PORT = int(os.getenv('WEBSOCKET_PORT', 8080))