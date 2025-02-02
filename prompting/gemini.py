import os
import google.generativeai as genai

def send_prompt(prompt):
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error during request: {e}"

# Esempio di utilizzo
prompt = '''

'''

result = send_prompt(prompt)
print(result)
