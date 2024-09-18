# AI-Powered-Sales-Representative-Email-Outreach-System
Overview
The AI-Powered SDR Email Outreach System is designed to automate and enhance the sales email outreach process for Sales Development Representatives (SDRs). By integrating AI with natural language processing, this system performs prospect research, generates personalized email drafts, reviews them against best practices, automates email sending via SMTP integration with Gmail, monitors email response and saves the mail log.

The goal of this project is to significantly reduce the time SDRs spend on repetitive tasks like researching prospects and crafting emails while increasing the effectiveness of outreach through personalized and optimized email content.

Features

1. Prospect Research Module
   Input: Prospect name, company name, and any additional information provided.
   Output: A comprehensive research report on the prospect and their company using APIs like Perplexity (or similar).
   Implementation: Uses external API calls to gather relevant details about the prospect.
2. Email Generation Module
   Input: Research report and product catalog (PDF/TXT).
   Output: AI-generated personalized email draft.
   Implementation: Uses an LLM to create a custom email using prospect research and product data.
3. Email Review Module
   Input: Generated email draft and sales email templates/winning emails (TXT format).
   Output: Reviewed and optimized email based on sales best practices.
   Implementation: Analyzes and enhances the email to match successful email templates.
4. Email Sending Module
   Functionality: Sends the final reviewed email to the prospect via Gmail using SMTP integration.
   Implementation: Uses Google’s SMTP server with app password-based authentication.
5. Email Monitoring: Monitors replies from prospects and can generate contextual follow-ups.
6. Data Storage: A simple local database to store prospect information and email history.

Setup instructions:

1. Install dependencies:
   pip install -r requirements.txt
2. Setup Gmail for Email Sending
   To send emails using Gmail, you’ll need to generate an app password:
   Enable 2-Step Verification in your Google Account.
   Generate an App Password from Google App Passwords.
   Use the 16-character password in the app when sending emails.
3. Run the streamlit frontend
   streamlit run frontend/app.py

How to Use the System

1. Input Prospect Details:
   Enter the prospect's name, company, and any additional details in the Streamlit frontend.
2. Upload Files:
   Upload the product catalog (PDF/TXT) and email templates (TXT).
3. Generate Email:
   Click the "Generate Email" button to create a personalized email using the research and product catalog.
4. Review Email:
   The system will review the generated email based on provided templates and best practices.
5. Send Email:
   Input your Gmail credentials and send the reviewed email to the prospect.
6. Monitor:
   Click the "Monitor" button to continuously monitor the email responses and save the logs.
