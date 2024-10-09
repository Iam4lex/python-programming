
# if, elif and else

"""
    syntax of if statement
    if condition:
        block of code
"""
# Example

number = 100
if number > 0:
    print(f"{number} is positive.")

"""
    else condition
    syntax
    if condition:
        block of code
    else:
        block of code
"""
# Example
number = -100
if number > 0:
    print(f"{number} is positive.")

else:
    print(f"{number} is negative.")

"""
    elif condition
    syntax
    if condition:
        block of code
    elif condition:
        block of code
    else:
        block of code
"""
# Example
temperature = -37

if temperature > 100:
    print("You have fever.")

elif temperature == 37:
    print("You are healthy.")

else:
    print("You have cold")