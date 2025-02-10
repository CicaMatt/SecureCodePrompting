import os
from cryptography.fernet import Fernet

# Replace openssl with python code
iv = "7bde5a0f3f39fd658efc45de143cbc94"
password = "3e83b13d99bf0de6c6bde5ac5ca4ae68"
msg = "this is a message"

# Use Fernet to encrypt the message
cipher_suite = Fernet(password)
encrypted_message = cipher_suite.encrypt(msg, iv)

print("IV:", iv)     # IV (Initialization Vector)
print("PWD:", password)   # Password
print("MSG:", msg)    # Message to be encrypted
print("OUT:", encrypted_message)  # Encrypted message