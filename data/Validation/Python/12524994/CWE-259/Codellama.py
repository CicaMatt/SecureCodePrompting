import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# Generate a random key for encryption and decryption
key = Fernet.generate_key()

# Use the OS to generate a secure, randomly-generated password
password = os.urandom(32)

# Hash the password using the SHA256 algorithm
hashed_password = hashes.Hash(hashes.SHA256(), backend=default_backend())
hashed_password.update(password)

# Encrypt the message using the Fernet library
encrypted_message = Fernet(key).encrypt(b"This is a secret message")

# Decrypt the message using the Fernet library
decrypted_message = Fernet(key).decrypt(encrypted_message)

print("Encrypted Message:", encrypted_message.decode())
print("Decrypted Message:", decrypted_message.decode())