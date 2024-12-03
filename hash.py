import hashlib

def hash_password(password: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()
password = input("Enter your password: ")
hashed_password = hash_password(password)
print(f"SHA-256 Hash: {hashed_password}")
