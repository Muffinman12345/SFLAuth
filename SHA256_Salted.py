import hashlib
import os

def generate_salt():
    # Generate a random 16-byte salt
    return os.urandom(16)

def hash_password(password, salt):
    # Combine the salt and password, then hash using SHA-256
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed_password

# Example usage
password = input("pswd: ")

# Generate a salt
salt = generate_salt()

# Hash the password with the salt
hashed_password = hash_password(password, salt)

print("Salt:", salt.hex())
print("Hashed Password:", hashed_password)
