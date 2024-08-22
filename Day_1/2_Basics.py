
print('Hello world!') # prints Hello world in the terminal

#           PYTHON INDENTATION
# Indentation reffers to the spaces at the begining of the code line
# Indentation in python is very important as shows block of code.
# Python will give you an error if you skip indentation

if 2 > 3:
    print('2 is greater than 3')

else:
    print('2 is less than 3') # prints 2 is greater than 3

#           PYTHON VARIABLES
# python variables are created when you assign values to it.

x = 10
message = "Hello there. Do you like coding ?"

#           PYTHON COMMENTS
# Python comments beigin with a # simbol. They are lines of code that exaplains python code and are not executed by the compiler.

# This line in a comment
print("The line above is a comment and it's not executed by the compiler")

#           CREATING VARIABLES
# A variable is created the moment you assign a value to it
x = 10
y = 20

print (x) # prints 10 on the terminal
print (y) # prints 20 in the terminal

#           CASTING 
# Casting is done if you want to change the datatype of a value
x = str(10) # The value 10 is changed from an integer to a string
y = int(3) # The value 3 is changed to integer datatype
z = float(20) # The value 20 is changed from an integer to a floating datatype

print(x) # prints 10
print(y) # prints 3
print(z) # prints 20.0

#           GET THE TYPE
# Get the type of a value

print(type(10)) # prints integer
print(type("Hello world")) # prints string
print(type(20.0)) # prints float
print(type(False)) #prints bool

#           VARIABLE NAMES
# Python is case sensitive 
a = 10
A = 20

# A will not overwrite a
print(a) # prints 10
print(A) # prints 20

# Python variables must start with a character or underscore character
# Python variables must not start with a number
# Examples of variables include
my_number = 10
myNumber = 20
_myNUmber = 30
MyNumber = 40

# Python  - Assign multiple variables
x, y, z = "Hello world", "Alex", "How are you"

print(x) # prints Hello world in the retminal
print(y) # prints Alex in the terminal
print(z) # prints How are you in the terminal

#           UNPACK A COLLECTION

fruits = ["Mango", "Apple", "Orange"]

x, y, z = fruits

print(fruits)
print(x)
print(y)
print(z)
