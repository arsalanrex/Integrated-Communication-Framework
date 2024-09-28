# users.py

import json

with open('users.json', 'r') as f:
    USERS = json.load(f)