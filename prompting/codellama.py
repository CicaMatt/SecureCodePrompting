from ollama import Client

def send_prompt_codellama(prompt):
    client = Client(host='http://localhost:11434')

    response=client.chat(model="codellama:13b", messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']

# prompt = ''''''
# print(send_prompt_codellama(prompt))