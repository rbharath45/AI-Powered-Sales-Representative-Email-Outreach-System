import json
import smtplib
from email.mime.text import MIMEText
import streamlit as st
import wikipediaapi

def extract_email_content_from_file(mail):

            lines = mail.splitlines()
            subject = ''
            body = ''
            subject_found = False
            
            for line in lines:
                if 'Subject:' in line:
                    subject = line.replace('Subject:', '').strip()
                    subject_found = True
                    continue
                if 'Major Changes Made' in line:
                    break
                if subject_found:
                    body += line + '\n'

            return subject, body.strip()

def save_email_data(to_email, subject, body): #saves the logs
            data = {
                'to_email': to_email,
                'subject': subject,
                'body': body,
                'status': 'sent'  
            }

            try:
                with open('sent_emails.json', 'a') as json_file:
                    json_file.write(json.dumps(data) + '\n')  
            except Exception as e:
                print(f'Error saving email data: {e}')
            return data

def generate_and_send_reply(to_email, subject): 
    # Create a formal reply message
    reply_subject = f"Re: {subject}"
    reply_body = """Dear Sir/Madam,

Thank you for your email. We have received your message and will get back to you shortly.

Best regards,
Bharath,
Sales Representative,
ABC Autoparts
"""
    EMAIL = "bharathabcautoparts@gmail.com"
    PASSWORD = "bjybznjzcauwdtci"
    SMTP_SERVER = "smtp.gmail.com"
    # Create the MIMEText object for the email
    msg = MIMEText(reply_body, "plain")
    msg["Subject"] = reply_subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    # Send the email via SMTP
    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        print(f"Sent reply to {to_email} with subject: {reply_subject}")
        st.write(f"Sent reply to {to_email} with subject: {reply_subject}")


def fetch_wikipedia_summary(topic): 
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent="YourAppName/1.0 (your-email@example.com)"
    )
    
    page = wiki_wiki.page(topic)
    
    if page.exists():
        return page.summary[:5000]
    else:
        return f"No information found on Wikipedia for {topic}."