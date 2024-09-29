# config/settings.py

import os
from dotenv import load_dotenv
import secrets
import base64
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
    # Generate a random 32-byte key and encode it to base64
    SECRET_KEY = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
else:
    # Ensure the provided key is in the correct format
    try:
        # Try to decode the key to check if it's valid base64
        base64.urlsafe_b64decode(SECRET_KEY)
    except:
        # If it's not valid base64, encode it
        SECRET_KEY = base64.urlsafe_b64encode(SECRET_KEY.encode()).decode()

# WebSocket settings
WEBSOCKET_HOST = os.getenv('WEBSOCKET_HOST', 'localhost')
WEBSOCKET_PORT = int(os.getenv('WEBSOCKET_PORT', 8080))