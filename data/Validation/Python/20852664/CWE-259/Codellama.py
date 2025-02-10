import os
from cryptography.fernet import Fernet

# Generate a new key and store it in an environment variable
key = Fernet.generate_key()
os.environ['CRYPTO_KEY'] = key.decode('utf-8')

def encrypt(message):
    # Load the encryption key from the environment variable
    key = os.environ['CRYPTO_KEY'].encode('utf-8')

    # Encrypt the message using the Fernet library
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode('utf-8'))

    return encrypted_message

def decrypt(ciphertext):
    # Load the encryption key from the environment variable
    key = os.environ['CRYPTO_KEY'].encode('utf-8')

    # Decrypt the message using the Fernet library
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(ciphertext).decode('utf-8')

    return decrypted_message

# Test the encryption and decryption functions
plaintext = 'This is a plaintext message'
encrypted_message = encrypt(plaintext)
decrypted_message = decrypt(encrypted_message)
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")