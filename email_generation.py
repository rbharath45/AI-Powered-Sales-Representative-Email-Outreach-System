import google.generativeai as genai
import os
import google.generativeai as genai

os.environ['GEMINI_API_KEY'] = 'AIzaSyBXt36aKNGiMHJ3PKymNm3Y4Lw-gYl1E_k'
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  #"response_mime_type": "text/plain"
}

def generate_email(product_catalog, research_report, prospect_name, company_name): #takes research report and product catalog to return generated email using gemini.

    prompt = f"Generate a personalized sales email to {prospect_name} at {company_name}. \The company faces these challenges: {research_report}. \Highlight these product features: {product_catalog}. \The email should ask for a meeting or demo and encourage them to buy the product based on their needs.My name is Bharath working as Sales Development Representative in ABC Autoparts. Don't give any of my other details."

    model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
          )
    chat_session = model.start_chat(
                    history=[
                    ]
                  )
    response = chat_session.send_message(prompt)

    return response.text



