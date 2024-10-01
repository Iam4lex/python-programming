
# A function to print the factorial of a number

def factorial_of_number():

    number = input("PLease enter the number: ")
    number = int(number)

    fact = 1

    for i in range(1, (number+1)):
        fact = fact*i
    
    print(f"The factorial of {number} is {fact}")

# Call the function
factorial_of_number()