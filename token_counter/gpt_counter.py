import tiktoken

def count_tokens(prompt):
    encoding = tiktoken.get_encoding("gpt-4o")
    tokens = encoding.encode(prompt)
    return len(tokens)
