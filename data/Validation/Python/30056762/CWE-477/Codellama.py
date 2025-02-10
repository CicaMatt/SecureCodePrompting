import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

# generate public and private keys
key = RSA.generate(1024, Random.new().read)

# export the public key for exchange
publickey = key.publickey

# encrypt message with public key and write ciphertext to file
encrypted = publickey.encrypt('encrypt this message', 32)
print 'encrypted message:', encrypted
with open('encryption.txt', 'w') as f:
    f.write(str(encrypted))

# read ciphertext from file and decrypt with private key
with open('encryption.txt', 'r') as f:
    message = f.read()
decrypted = key.decrypt(message)
print 'decrypted', decrypted