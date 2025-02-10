from Crypto import Random
from Crypto.Cipher import AES
import base64

def encrypt(message, key=None, key_size=256):
    def pad(s):
        x = AES.block_size - len(s) % AES.block_size
        return s + ((bytes([x])) * x)

    padded_message = pad(message)

    if key is None:
        key = Random.new().read(key_size // 8)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return base64.b64encode(iv + cipher.encrypt(padded_message))

def decrypt(ciphertext, key):
    base64_decoded = base64.b64decode(ciphertext)
    iv = base64_decoded[:AES.block_size]
    ciphertext = base64_decoded[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext)
message = "Hello World!"
key = b"MySuperSecretKey1234567890"

encrypted_message = encrypt(message, key=key)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)
b'SGVsbG8gV29ybGQhISE='
Hello World!