import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# generate a random initialization vector (IV) of the correct size
def generate_iv(key):
    return get_random_bytes(AES.block_size)

# encrypt a message using AES with the specified key and IV
def encrypt(message, key):
    iv = generate_iv(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

# decrypt a message using AES with the specified key and IV
def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext[AES.block_size:])