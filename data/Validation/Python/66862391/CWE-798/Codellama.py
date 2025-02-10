from cryptography.fernet import Fernet

# Generate a random salt for password hashes
salt = os.urandom(32)

# Generate a key from the password and salt
key =Fernet.generate_key(password, salt)

# Encrypt the message using AES-128-CBC with the generated key
ciphertext = Fernet.encrypt(message, key)

# Decrypt the encrypted message back to plain text using the same key
plaintext = Fernet.decrypt(ciphertext, key)