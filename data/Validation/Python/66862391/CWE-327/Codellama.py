import os, base64, hashlib

def generate_key(password):
    # Generate a SHA-256 digest from the password
    digest = hashlib.sha256(password.encode()).digest()
    # Convert the digest to a 16-byte key using AES-128 CBC
    return bytes([x for x in base64.b32decode(digest)])[0:16]

def generate_iv():
    # Generate a random initialization vector (IV)
    return os.urandom(16)

def encrypt(key, iv, message):
    # Encrypt the message using AES-128 CBC with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    encrypted = base64.b32encode(cipher.encrypt(message))
    return encrypted

def decrypt(key, iv, message):
    # Decrypt the message using AES-128 CBC with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = base64.b32decode(cipher.decrypt(message))
    return decrypted
key = generate_key("my-secret-password")
iv = generate_iv()

message = "this is a message"
encrypted = encrypt(key, iv, message)
print("Encrypted:", encrypted)

decrypted = decrypt(key, iv, encrypted)
print("Decrypted:", decrypted)