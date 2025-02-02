from ollama import Client

client = Client(host='http://localhost:11434')

prompt='''

'''

response=client.chat(model="codellama:13b", messages=[
    {
        'role': 'user',
        'content': prompt,
    },
])

print(response['message']['content'])
