import os
import google.generativeai as genai

def count_tokens(prompt):
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    token_count = model.count_tokens(prompt)
    return token_count