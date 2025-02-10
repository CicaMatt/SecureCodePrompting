import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_aes_cbc(message, key, iv):
    """Encrypts a message using AES-128-CBC with PKCS#7 padding and returns a base64 encoded string."""

    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(message.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(ciphertext).decode('utf-8')



iv = "7bde5a0f3f39fd658efc45de143cbc94"
password = "3e83b13d99bf0de6c6bde5ac5ca4ae68"
msg = "this is a message"

encrypted_message = encrypt_aes_cbc(msg, password, iv)

print(f"IV: {iv}")
print(f"PWD: {password}")
print(f"MSG: {msg}")
print(f"OUT: {encrypted_message}")