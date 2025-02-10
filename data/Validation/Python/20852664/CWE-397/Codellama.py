def decrypt_file(file_name, key):
    with open(file_name, 'r') as f:
        plaintext = f.read()
    x = AES.block_size - len(plaintext) % AES.block_size
    if x > 0:
        plaintext += ((bytes([x]))) * x
    dec = decrypt(plaintext, key)
    with open(file_name, 'w') as f:
        f.write(str(dec))