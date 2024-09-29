# app.py

import os
import json
import asyncio
import traceback
import aiohttp
from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from email_service.email_manager import EmailManager
from chat_service.chat_manager import ChatManager
from config.settings import SECRET_KEY, USERS, WEBSOCKET_HOST, WEBSOCKET_PORT, DATABASE_URI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
email_manager = EmailManager()
chat_manager = ChatManager()

async def index(request):
    with open(os.path.join(BASE_DIR, 'templates', 'index.html'), 'r') as file:
        return web.Response(text=file.read(), content_type='text/html')

async def static_files(request):
    path = request.match_info['path']
    try:
        with open(os.path.join(BASE_DIR, 'static', path), 'rb') as file:
            return web.Response(body=file.read(), content_type='text/css')
    except FileNotFoundError:
        return web.Response(status=404)

async def login(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')
    if username in USERS and USERS[username]['password'] == password:
        session = await get_session(request)
        session['user'] = username
        return web.json_response({'success': True})
    return web.json_response({'success': False})

async def logout(request):
    session = await get_session(request)
    session.clear()
    return web.json_response({'success': True})

async def send_email(request):
    data = await request.json()
    session = await get_session(request)
    sender = session.get('user')
    if not sender:
        return web.json_response({'success': False, 'error': 'Not authenticated'})
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    try:
        success = await email_manager.send_email(sender, recipient, subject, body)
        if success:
            return web.json_response({'success': True})
        else:
            return web.json_response({'success': False, 'error': 'Failed to send email'})
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        print(traceback.format_exc())
        return web.json_response({'success': False, 'error': str(e)})

async def get_emails(request):
    session = await get_session(request)
    user = session.get('user')
    if not user:
        return web.json_response({'success': False, 'error': 'Not authenticated'})
    emails = await email_manager.get_emails(user)
    return web.json_response({'success': True, 'emails': emails})

async def send_chat(request):
    data = await request.json()
    session = await get_session(request)
    sender = session.get('user')
    if not sender:
        return web.json_response({'success': False, 'error': 'Not authenticated'})
    recipient = data.get('recipient')
    message = data.get('message')
    success = await chat_manager.send_message(USERS[sender]['mobile'], recipient, message)
    return web.json_response({'success': success})

async def get_chats(request):
    session = await get_session(request)
    user = session.get('user')
    if not user1:
        return web.json_response({'success': False, 'error': 'Not authenticated'})
    #user2 = request.query.get('user')
    messages = await chat_manager.get_messages(USERS[user]['mobile'])
    return web.json_response({'success': True, 'messages': messages})

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    session = await get_session(request)
    user = session.get('user')
    if not user:
        await ws.close()
        return ws

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            data = json.loads(msg.data)
            if data['type'] == 'email':
                emails = await email_manager.get_emails(user)
                await ws.send_json({'type': 'email', 'emails': emails})
            elif data['type'] == 'chat':
                messages = await chat_manager.get_messages(data.get('recipient'))
                await ws.send_json({'type': 'chat', 'messages': messages})
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'WebSocket connection closed with exception {ws.exception()}')

    return ws

app = web.Application()
setup(app, EncryptedCookieStorage(SECRET_KEY))

app.router.add_get('/', index)
app.router.add_get('/static/{path:.*}', static_files)
app.router.add_post('/login', login)
app.router.add_post('/logout', logout)
app.router.add_post('/send_email', send_email)
app.router.add_get('/get_emails', get_emails)
app.router.add_post('/send_chat', send_chat)
app.router.add_get('/get_chats', get_chats)
app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    web.run_app(app, host=WEBSOCKET_HOST, port=WEBSOCKET_PORT)
