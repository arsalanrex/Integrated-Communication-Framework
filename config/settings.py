import os
from dotenv import load_dotenv
import base64
from cryptography.fernet import Fernet

load_dotenv()

EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 1025))
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', 'your_username')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password')

CHAT_SERVER = os.getenv('CHAT_SERVER', 'localhost')
CHAT_PORT = int(os.getenv('CHAT_PORT', 5222))

DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///integrated_communication.db')

# Generate a proper SECRET_KEY if not provided
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = Fernet.generate_key().decode()
print(SECRET_KEY)

# User management
USERS = {
    "user1": {
        "email": "user1@example.com",
        "password": "password1",
        "mobile": "+1234567890"
    },
    "user2": {
        "email": "user2@example.com",
        "password": "password2",
        "mobile": "+0987654321"
    }
}

# WebSocket settings
WEBSOCKET_HOST = os.getenv('WEBSOCKET_HOST', 'localhost')
WEBSOCKET_PORT = int(os.getenv('WEBSOCKET_PORT', 8080))