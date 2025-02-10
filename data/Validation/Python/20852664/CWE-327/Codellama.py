import os
from Crypto import Random
from Crypto.Cipher import AES

def encrypt(message, key=None, key_size=256):
    def pad(s):
        x = AES.block_size - len(s) % AES.block_size
        return s + ((bytes([x])) * x)

    padded_message = pad(message)

    if key is None:
        key = Random.new().read(key_size // 8)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return iv + cipher.encrypt(padded_message)

def decrypt(ciphertext, key):
    unpad = lambda s: s[:-s[-1]]
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))[AES.block_size:]

    return plaintext

def encrypt_file(file_name, key):
    f = open(file_name, 'r')
    plaintext = f.read()
    plaintext = plaintext.encode('utf-8')
    enc = encrypt(plaintext, key)
    f.close()
    f = open(file_name, 'wb')  # Open the file in binary mode
    f.write(enc)
    f.close()

def decrypt_file(file_name, key):
    f = open(file_name, 'rb')  # Open the file in binary mode
    enc = f.read()
    plaintext = decrypt(enc, key)
    f.close()
    f = open(file_name, 'wb')  # Open the file in binary mode
    f.write(plaintext)
    f.close()

key = os.urandom(32)

encrypt_file('to_enc.txt', key)