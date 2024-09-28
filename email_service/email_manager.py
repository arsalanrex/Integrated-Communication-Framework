# email_service/email_manager.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_SERVER, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, USERS
from email_service.email_storage import EmailStorage
import traceback
import asyncio

email_storage = EmailStorage()


class EmailManager:
    def __init__(self):
        self.server = EMAIL_SERVER
        self.port = EMAIL_PORT
        self.username = EMAIL_USERNAME
        self.password = EMAIL_PASSWORD

    async def send_email(self, sender, recipient, subject, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = USERS[sender]['email']

            # Check if recipient is an email address or a username
            if '@' in recipient:
                msg['To'] = recipient
            else:
                msg['To'] = USERS[recipient]['email']

            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Use asyncio to run the SMTP operations in a separate thread
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self._send_smtp, msg)

            await email_storage.store_email(sender, recipient, subject, body)
            print(f"Email sent from {sender} to {recipient}")
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            print(traceback.format_exc())
            return False

    def _send_smtp(self, msg):
        with smtplib.SMTP(self.server, self.port) as server:
            server.sendmail(msg['From'], msg['To'], msg.as_string())

    async def get_emails(self, user):
        return await email_storage.get_emails(user)

    async def mark_as_read(self, user, email_id):
        return await email_storage.mark_as_read(user, email_id)

    async def delete_email(self, user, email_id):
        return await email_storage.delete_email(user, email_id)