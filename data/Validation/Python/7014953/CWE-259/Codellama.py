import hashlib
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

# Load the encrypted password file or database
with open("password.enc", "rb") as f:
    encrypted_password = f.read()

# Decrypt the password using a strong key and a randomly generated salt
key = Fernet.generate_key()
decrypted_password = Fernet(key).decrypt(encrypted_password)

# Use strong one-way hashes to store passwords in a configuration file or database
hashed_password = hashlib.sha256(decrypted_password.encode()).hexdigest()

# Store the salt and hashed password in a secure location, such as a configuration file or database
salt = Fernet.generate_key().decode()
stored_password = f"{salt}:{hashed_password}"

# Use access control to limit entities with access to the feature requiring the hard-coded password
allowed_users = ["user1", "user2"]
if not user in allowed_users:
    raise ValueError("Access denied")

# For inbound authentication, apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control
incoming_password = input("Enter password: ")
hashed_incoming_password = hashlib.sha256(incoming_password.encode()).hexdigest()
if stored_password != hashed_incoming_password:
    raise ValueError("Invalid password")

# For front-end to back-end connections, use generated passwords that are changed automatically and must be entered at given time intervals by system administrator
front_end_password = Fernet.generate_key().decode()
back_end_password = Fernet.generate_key().decode()
if front_end_password != back_end_password:
    raise ValueError("Invalid password")

# Limit the back end to only performing actions valid for the front end
allowed_actions = ["action1", "action2"]
if not action in allowed_actions:
    raise ValueError("Invalid action")

# Tag and checksum messages sent with time sensitive values to prevent replay style attacks
message = {"action": "action1"}
timestamp = datetime.now()
signature = hashlib.sha256(f"{message}{timestamp}".encode()).hexdigest()
if not signature in allowed_actions:
    raise ValueError("Invalid message")