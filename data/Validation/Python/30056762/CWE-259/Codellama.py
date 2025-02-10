import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

# generate a key pair with a random generator
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private keys

publickey = key.publickey # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message:', encrypted #ciphertext

f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open ('encryption.txt', 'r')
message = f.read()

# use a secure random number generator to generate the decryption key
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private keys

decrypted = key.decrypt(message)

print 'decrypted', decrypted

f = open ('encryption.txt', 'w')
f.write(str(decrypted))
f.close()