import sqlite3
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# --- KEY DERIVATION ---
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


# --- DATABASE OPERATIONS ---
DATABASE_FILE = "credentials.db"  # Store in a less obvious location if possible

def create_database(password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    f = Fernet(key)
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS credentials
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, salt BLOB)''')
    conn.commit()
    conn.close()
    return f, salt


def store_credentials(f, username, password_to_store, salt):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    encrypted_username = f.encrypt(username.encode())
    encrypted_password = f.encrypt(password_to_store.encode())
    c.execute("INSERT INTO credentials (username, password, salt) VALUES (?, ?, ?)",
              (encrypted_username, encrypted_password, salt))
    conn.commit()
    conn.close()



def retrieve_credentials(password):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT salt FROM credentials WHERE id = 1") # Assumes only one entry
    result = c.fetchone()
    conn.close()
    if not result:
        return None, None  # Handle case where no credentials are found
    salt = result[0]
    key = derive_key(password, salt)
    f = Fernet(key)
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT username, password FROM credentials WHERE id = 1")  # Assumes only one entry
    result = c.fetchone()
    conn.close()

    if result:
      try: # Crucial try/except to handle incorrect passwords
        username = f.decrypt(result[0]).decode()
        password = f.decrypt(result[1]).decode()
        return username, password
      except:
        return None, None # Or raise a custom exception
    else:
        return None, None

# --- EXAMPLE USAGE ---

# FIRST TIME SETUP - creates DB, encrypts and stores credentials
db_password = "YourStrongDatabasePassword" # Different from service password
f, salt = create_database(db_password)
store_credentials(f, "your_service_username", "your_service_password", salt)


# LATER RETRIEVAL during script execution
retrieved_username, retrieved_password = retrieve_credentials(db_password)

if retrieved_username and retrieved_password:
    print("Retrieved Username:", retrieved_username)
    print("Retrieved Password:", retrieved_password)

    # Now use retrieved_username and retrieved_password with the 3rd party service

else:
    print("Failed to retrieve credentials. Incorrect password?")