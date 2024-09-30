import bcrypt

# Password to hash
password = 'iamalex'.encode()  # Convert to bytes

# Generate salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print("Hashed password:", hashed_password.decode())
