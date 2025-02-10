import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(message, key):
    # Generate a random initialization vector (IV) for each encryption operation
    iv = get_random_bytes(AES.block_size)
    
    # Use the same key and IV for both encryption and decryption
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the message to a multiple of the block size (16 bytes)
    padded_message = pad(message, AES.block_size)
    
    # Encrypt the message and return the ciphertext
    return base64.b64encode(iv + cipher.encrypt(padded_message))

def decrypt(ciphertext, key):
    # Extract the initialization vector (IV) from the ciphertext
    iv = ciphertext[:AES.block_size]
    
    # Use the same key and IV for both encryption and decryption
    decipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the message and unpad it to the original length
    return unpad(decipher.decrypt(base64.b64decode(ciphertext[AES.block_size:])), AES.block_size)