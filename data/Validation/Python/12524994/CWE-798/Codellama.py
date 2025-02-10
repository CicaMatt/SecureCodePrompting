The following is a solution to the problem statement provided:

import os, hashlib
from Crypto.Cipher import AES
 
def encrypt(message, key):
    """Encrypts message using AES with key and returns encrypted bytes"""
    # generate random IV for encryption
    iv = os.urandom(16)
     
    # create cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
 
    # encrypt message using cipher
    encrypted_message = cipher.encrypt(message)
 
    # return concatenated IV and encrypted message
    return iv + encrypted_message
 
def decrypt(encrypted_message, key):
    """Decrypts encrypted_message using AES with key and returns decrypted bytes"""
    # extract IV from beginning of encrypted_message
    iv = encrypted_message[:16]
     
    # create cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
 
    # decrypt message using cipher
    decrypted_message = cipher.decrypt(encrypted_message[16:])
 
    # return decrypted message bytes
    return decrypted_message
 
# example usage of encrypt and decrypt functions
message = b"Hello, world!"
key = hashlib.sha256("mysecretpassword").digest()
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)