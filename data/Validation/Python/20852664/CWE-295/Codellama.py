def decrypt_file(file_name, key):
    f = open(file_name, 'r')
    plaintext = f.read()
    # No need to pad the plaintext before encryption
    enc = encrypt(plaintext, key)
    f.close()
    f = open(file_name, 'w')
    f.write(str(enc))
    f.close()