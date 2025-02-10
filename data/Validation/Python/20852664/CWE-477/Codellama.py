from Crypto import Random
from Crypto.Cipher import AES
import os

def encrypt(message, key=None, key_size=256):
    def pad(s):
        x = AES.block_size - len(s) % AES.block_size
        return s + ((bytes([x])) * x)

    padded_message = pad(message)

    if key is None:
        key = os.urandom(key_size // 8)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_GCM, iv=iv, tag_len=16)

    return iv + cipher.encrypt(padded_message)

def decrypt(ciphertext, key):
    unpad = lambda s: s[:-s[-1]]

    iv = ciphertext[:AES.block_size]
    tag = ciphertext[AES.block_size:]

    cipher = AES.new(key, AES.MODE_GCM, iv=iv, tag_len=16)
    decrypted = cipher.decrypt(tag)

    return unpad(decrypted)