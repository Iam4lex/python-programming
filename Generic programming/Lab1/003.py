"""3.Write a Python program to find the digits which are absent in a given mobile number."""

mobile_number = input("Enter your mobile number: ")
digits = "0123456789"
absent_digits = []

for digit in digits:
    if digit not in mobile_number:
        absent_digits.append(digit)


print(", ".join(absent_digits))
    

