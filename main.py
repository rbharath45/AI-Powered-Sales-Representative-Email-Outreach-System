# backend/main.py
from fastapi import FastAPI
from .research import generate_prospect_research_report
from .email_generation import generate_email
from .email_review import review_email
from .email_sender import send_email

app = FastAPI()

@app.post("/research")
async def research(prospect_name: str, company_name: str, additional_info: str):
    return generate_prospect_research_report(prospect_name, company_name, additional_info)

@app.post("/generate_email")
async def generate(product_catalog, research_data, prospect_name, company_name):
    return generate_email(product_catalog, research_data, prospect_name, company_name)

@app.post("/review_email")
async def review(generated_email, template_text):
    return review_email(generated_email, template_text)

@app.post("/send_email")
async def send(recipient_email, reviewed_email, sender_email, app_password):
    return send_email(recipient_email, reviewed_email, sender_email, app_password)
