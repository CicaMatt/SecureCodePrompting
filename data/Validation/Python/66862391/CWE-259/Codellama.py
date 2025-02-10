import os
from cryptography.fernet import Fernet

# Generate a key and initialize the Fernet object
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt the message using the Fernet object
encrypted_msg = f.encrypt(b"this is a message")

# Print the encrypted message
print(encrypted_msg)