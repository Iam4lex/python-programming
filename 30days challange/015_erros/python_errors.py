
# Python has alot of types of errors that we can make when writing our code.

# 1. Module not found error

# import maths # This will print an error
import math # This is correct

# 2. Attriubute error
math.PI # This will print an error AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?


# 3. SyntaxError

# This will raise a SyntaxError due to the missing colon at the end of the if statement.
# if 5 > 2
#     print("5 is greater than 2")

# Correct version:
if 5 > 2:
    print("5 is greater than 2")

# 4. IndentationError

# This will raise an IndentationError because the second print statement is not properly indented.
# if 5 > 2:
# print("5 is greater than 2")

# Correct version:
if 5 > 2:
    print("5 is greater than 2")

# 5. NameError

# Trying to use a variable that hasn’t been defined will raise a NameError.
# print(number)  # NameError: name 'number' is not defined

# Correct version:
number = 10
print(number)  # This will print 10

# 6. TypeError

# This will raise a TypeError because we can't concatenate a string with an integer.
# age = 25
# print("I am " + age + " years old")

# Correct version:
age = 25
print("I am " + str(age) + " years old")  # Convert the integer to a string

# 7. ValueError

# Trying to convert an invalid string to an integer will raise a ValueError.
# int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

# Correct version:
valid_number = int("123")  # This will correctly convert the string to an integer
print(valid_number)  # Output: 123
