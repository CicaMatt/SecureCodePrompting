import sqlite3
from pycrypto import encrypt, decrypt

# Encrypt the credentials using AES
cipher = encrypt(b"YOUR_CREDENTIALS", b"SECRET_KEY")

# Store the encrypted credentials in a SQLite database
conn = sqlite3.connect("credentials.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS credentials (id integer PRIMARY KEY, username text, password text)")
c.execute("INSERT INTO credentials VALUES (?, ?)", [cipher])
conn.commit()
conn.close()

# Decrypt the credentials when using them
def get_credentials():
    conn = sqlite3.connect("credentials.db")
    c = conn.cursor()
    cipher = c.execute("SELECT password FROM credentials WHERE id=1").fetchone()[0]
    username, password = decrypt(cipher, b"SECRET_KEY").decode().split(":")
    return (username, password)