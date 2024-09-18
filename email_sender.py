import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import imaplib
import email
from email.header import decode_header
import streamlit as st
import json
from utils import extract_email_content_from_file,save_email_data,generate_and_send_reply

logging.basicConfig(level=logging.INFO)


def send_email(recipient_email: str, reviewed_email: str, sender_email: str, app_password: str): #takes reviewed mail, recipient mail, sender mail, app password and sends email. And saves the log.
    logging.info(f"Attempting to send email to {recipient_email}")
    subject, body = extract_email_content_from_file(reviewed_email)
    save_email_data("rbharath2310@gmail.com", subject, body)
    st.write(subject, body)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)  # Login with the app password
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send email
            logging.info(f"Email successfully sent to {recipient_email}")
    
    except Exception as e:
        logging.error(f"Failed to send email. Error: {e}")

def check_for_new_mail(): #checks for reply mails from particular mail id and send response for replies.
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    SMTP_SERVER = "smtp.gmail.com"
    EMAIL = "bharathabcautoparts@gmail.com"
    PASSWORD = "bjybznjzcauwdtci"
    SPECIFIC_EMAIL = "rbharath2310@gmail.com"
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()

    for mail_id in email_ids:
        status, msg_data = mail.fetch(mail_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")

                from_email = email.utils.parseaddr(msg.get("From"))[1]
                print("mail from:", from_email)
                st.write("mail from:", from_email)
                if from_email == SPECIFIC_EMAIL:
                    print(f"New email from: {from_email}, Subject: {subject}")
                    st.write(f"New email from: {from_email}, Subject: {subject}")

                    generate_and_send_reply(from_email, subject)

    mail.logout()

