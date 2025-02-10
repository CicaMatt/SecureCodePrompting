import cryptography
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.backends import default_backend

# Initialize the encryption key and IV
key = b"3e83b13d99bf0de6c6bde5ac5ca4ae68"
iv = b"7bde5a0f3f39fd658efc45de143cbc94"

# Load the encryption algorithm and create an encryptor object
algorithm = ciphers.AES(key)
encryptor = algorithm.new_ctr_encrypter(iv, default_backend())

# Encrypt the message using the encryptor object
msg = b"this is a message"
ciphertext = encryptor.update(msg) + encryptor.finalize()

# Print the output
print("IV:", iv.hex())
print("PWD:", key.hex())
print("MSG:", msg.decode("utf-8"))
print("OUT:", ciphertext.hex())