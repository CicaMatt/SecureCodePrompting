import os
from cryptography.fernet import Fernet

def encrypt(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt(encrypted):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted).decode()
    return decrypted