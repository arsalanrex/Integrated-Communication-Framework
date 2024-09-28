import base64
import os

# Generate a 32-byte key
key = base64.urlsafe_b64encode(os.urandom(32))
print(key.decode())