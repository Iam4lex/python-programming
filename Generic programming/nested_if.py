
# Nested if statements


role = input("Enter user role (admin/user): ")
status = input("Enter account status (active/inactive): ")

if role == "admin":
    if status == "active":
        print("Access granted to admin.")
    else:
        print("Admin access denied. Account is inactive.")
elif role == "user":
    if status == "active":
        print("Access granted to user.")
    else:
        print("User access denied. Account is inactive.")
else:
    print("Access denied. Unknown role.")
