
# Print the factorial of a number

number = input("Please enter the number to check the factorial: ")
number = int(number)

fact = 1

for i in range(1, number+1):
    fact = fact*i

print(f"The factorial of {number} is {fact}")