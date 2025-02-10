import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(message, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message.encode())

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext[AES.block_size:]).decode()

# Example usage
message = "Hello World!"
key = get_random_bytes(16)

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)