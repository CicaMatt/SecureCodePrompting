import cryptography
from cryptography.fernet import Fernet

# Load the encryption key from a secure location, such as a file or environment variable
encryption_key = "my-secret-encryption-key"

# Create a Fernet instance with the encryption key
f = Fernet(encryption_key)

# Encrypt the username and password combo using the Fernet instance
encrypted_username = f.encrypt("my_username")
encrypted_password = f.encrypt("my_password")

# Save the encrypted data to a file or database
with open("encrypted_data.txt", "wb") as f:
    f.write(encrypted_username)
    f.write(encrypted_password)
# Load the encrypted data from a file or database
with open("encrypted_data.txt", "rb") as f:
    encrypted_username = f.read()
    encrypted_password = f.read()

# Create a Fernet instance with the encryption key
f = Fernet(encryption_key)

# Decrypt the username and password combo using the Fernet instance
decrypted_username = f.decrypt(encrypted_username)
decrypted_password = f.decrypt(encrypted_password)

print("Decrypted username:", decrypted_username)
print("Decrypted password:", decrypted_password)