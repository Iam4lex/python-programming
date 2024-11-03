
# Factorial of a number

"""
    Algorithm
    start
    initialize fact = 1
    accept input number from the user
    loop the number+1 -> for num in range(1, number+1)
    multiply fact by num
    stop
"""

fact = 1

number = int(input("Enter a number: "))

for num in range(1, number+1):
    fact *= num

print(f"The factorial of {number} is {fact}")