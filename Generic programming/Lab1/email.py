

email = input("Please enter the email: ")
char = email.find("@")
dot= email.rfind(".")
username = email[:char]
companyName = email[char+1:dot]

print("Username: ",username.upper())
print("Company: ",companyName.title())