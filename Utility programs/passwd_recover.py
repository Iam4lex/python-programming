import sys
import bcrypt

# Check if a hashed password argument is provided
if len(sys.argv) < 2:
    print("Usage: python passwd_recover.py <hashed_password>")
    sys.exit(1)  # Exit the program if no argument is provided

hashed_password = sys.argv[1].encode()  # Pass the hashed password as a command-line argument

# Open the file containing passwords
with open('passwords.txt', 'r') as passfile:
    # Loop through each line (each word) in the file
    for word in passfile.readlines():
        if bcrypt.checkpw(word.strip().encode(), hashed_password):
            print("The password is:", word.strip())
            break
