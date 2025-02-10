from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
from base64 import b64encode, b64decode

def encrypt(message, key):
    """Encrypts a message using AES-256 in CBC mode.

    Args:
        message: The message to be encrypted (string or bytes).
        key: The encryption key (string or bytes). Should be a strong, randomly generated key.

    Returns:
        A dictionary containing the IV (Initialization Vector) and the ciphertext, both base64 encoded.
        Returns None if an error occurs.
    """
    try:
        # Convert message and key to bytes if necessary
        if isinstance(message, str):
            message = message.encode('utf-8')
        if isinstance(key, str):
            key = key.encode('utf-8')

        # Generate a 256-bit key from the provided key using SHA-256
        key = sha256(key).digest() 

        # Generate a random 16-byte IV
        iv = get_random_bytes(AES.block_size)

        # Create a cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Pad the message to a multiple of the block size
        padding_length = AES.block_size - len(message) % AES.block_size
        message += bytes([padding_length]) * padding_length

        # Encrypt the message
        ciphertext = cipher.encrypt(message)

        # Encode IV and ciphertext using base64
        return {
            'iv': b64encode(iv).decode('utf-8'),
            'ciphertext': b64encode(ciphertext).decode('utf-8')
        }
    except Exception as e:
        print(f"Encryption error: {e}")
        return None



def decrypt(encrypted_message, key):
    """Decrypts a message encrypted with AES-256 in CBC mode.

    Args:
        encrypted_message: A dictionary containing the base64 encoded IV and ciphertext.
        key: The decryption key (string or bytes). Must be the same key used for encryption.

    Returns:
        The decrypted message as a string.
        Returns None if an error occurs.

    """
    try:
         # Convert key to bytes if necessary
        if isinstance(key, str):
            key = key.encode('utf-8')

        # Generate the 256-bit key from the provided key using SHA-256
        key = sha256(key).digest()

        # Decode IV and ciphertext from base64
        iv = b64decode(encrypted_message['iv'])
        ciphertext = b64decode(encrypted_message['ciphertext'])

        # Create a cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)


        # Decrypt the message
        plaintext_padded = cipher.decrypt(ciphertext)


        # Remove padding
        padding_length = plaintext_padded[-1]
        plaintext = plaintext_padded[:-padding_length]

        # Return the decrypted message as a string
        return plaintext.decode('utf-8')

    except Exception as e:
        print(f"Decryption error: {e}")
        return None




# Example usage:
key = get_random_bytes(32) # Generate a strong, random 32-byte key – store this securely!
message = "This is a secret message."

encrypted_message = encrypt(message, key)
if encrypted_message:
    decrypted_message = decrypt(encrypted_message, key)
    if decrypted_message:
        print("Original message:", message)
        print("Decrypted message:", decrypted_message)