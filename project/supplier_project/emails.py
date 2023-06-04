#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import os
import smtplib
import getpass

def generate_email(sender):
    message = EmailMessage()
    message['From'] = "automation@example.com"
    message['To'] = sender
    message['Subject'] = "Upload Completed - Online Fruit Store"
    body = """
        All fruits are uploaded to our website successfully. A detailed list is attached to this email.
    """
    message.set_content(body)
    attachment_path = "/tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as f:
        message.add_attachment(f.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    return message

def send_email(sender, message):
    mail_server = smtplib.SMTP("SMTP.example.com")
    mail_pass = getpass.getpass('Password? ')
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == "__main__":
    sender = "student-03-bc9dff989976@example.com"
    message = generate_email(sender)
    send_email(sender, message)