import hashlib
password = "hello123"
hashed = hashlib.md5(password.encode()).hexdigest()
print("Hashed password:", hashed)
