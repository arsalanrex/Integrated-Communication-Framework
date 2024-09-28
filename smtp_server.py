# integrated_communication/smtp_server.py

import asyncio
from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f'Received email from: {envelope.mail_from}')
        print(f'Received email to: {envelope.rcpt_tos}')
        print(f'Message:\n{envelope.content.decode("utf-8", errors="replace")}')
        return '250 Message accepted for delivery'

def run_smtp_server():
    controller = Controller(CustomSMTPHandler(), hostname='localhost', port=1025)
    controller.start()
    print('SMTP server started on port 1025...')
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print('SMTP server stopped.')
        controller.stop()

if __name__ == '__main__':
    run_smtp_server()