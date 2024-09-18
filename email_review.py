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

def review_email(generated_email: str, email_templates: str) -> str: #takes generated email, template as input and generate reviewed email using gemini.
    prompt = f"Review the following email based on best practices and generate an improved draft:{generated_email} Use these templates as a reference for best practices:{email_templates}. Give the major changes made."

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