import os
from cryptography.fernet import Fernet

def encrypt(message):
    # Generate a new key for encryption
    key = Fernet.generate_key()
    ciphertext = Fernet(key).encrypt(message)
    return ciphertext

def decrypt(ciphertext):
    # Load the key from an environment variable
    key = os.environ['ENCRYPTION_KEY']
    message = Fernet(key).decrypt(ciphertext)
    return message

# Example usage:
username = 'user@example.com'
password = 'secret_password'
encrypted_message = encrypt(f'{username}:{password}')
print(encrypted_message)
export ENCRYPTION_KEY=$(fernet-generate)