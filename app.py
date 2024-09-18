import streamlit as st
from research import generate_prospect_research_report
from email_generation import generate_email
from email_review import review_email
from email_sender import send_email 
from email_sender import check_for_new_mail

import time

st.title("SDR Email Outreach Automation")

if 'new_fields' not in st.session_state:
    st.session_state['new_fields'] = False


# Input fields
prospect_name = st.text_input("Prospect Name")
company_name = st.text_input("Company Name")
additional_info = st.text_area("Additional Information", "")

# File uploads
product_catalog = st.file_uploader("Upload Product Catalog", type=['pdf', 'txt'])
email_templates = st.file_uploader("Upload Email Templates", type=['txt'])

generate_button = st.button("Generate Email")

if generate_button:
    if product_catalog and email_templates:
        # Process inputs
        template_text = email_templates.read().decode('utf-8')
        # Prospect research
        research_data = generate_prospect_research_report(prospect_name, company_name, additional_info)
        st.write("--Research Data: \n-", research_data)

        # Email generation
        product_text = product_catalog.read().decode('utf-8')
        generated_email = generate_email(product_catalog, research_data, prospect_name, company_name)
        st.write("--Generated Email: \n-", generated_email)

        # Email review
        reviewed_email = review_email(generated_email, template_text)
        st.write("--Reviewed Email: \n-", reviewed_email)

    else:
        st.error("Please upload a product catalog and email templates.")

send_button = st.button("Send Email")

# Email sending
if send_button:
    st.session_state['new_fields'] = True

if st.session_state['new_fields']:
    recipient_email = st.text_input("Recipient Email")
    sender_email = "bharathabcautoparts@gmail.com"
    app_password = "bjybznjzcauwdtci"
    
    if recipient_email and sender_email and app_password:
        research_data = generate_prospect_research_report(prospect_name, company_name, additional_info)
        generated_email = generate_email(product_catalog, research_data, prospect_name, company_name)
        template_text = email_templates.read().decode('utf-8')
        reviewed_email = review_email(generated_email, template_text)
        send_email(recipient_email, reviewed_email, sender_email, app_password)
        st.success("Email Sent!")

monitor_button = st.button("Monitor")
if monitor_button:
    st.write(f"Monitoring for new emails from {recipient_email}...")
    while True:
        check_for_new_mail()
        time.sleep(10)
