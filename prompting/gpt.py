import os
from openai import OpenAI

def send_prompt_gpt(prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o",
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error during request: {e}"

# prompt = ''''''
# print(send_prompt_gpt(prompt))
