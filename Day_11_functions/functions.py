# FUNCTIONS

# A function in python is declared or defined using the def keyword

# syntax
# Declaring a function
# def function_name():
  #  codes
  #  codes
# Calling a function
#function_name()

# example

def my_function():
    # block of code goes here.
    print("Helllo world!")

# calling the fuction
my_function()

# FUNCTIONS WITHOUT PARAMETERS
# functions can be declared without parameters

def function_without_parameter():
    first_name = 'Alex'
    second_name = 'Mwangi'

    full_name = first_name + second_name

    print(f"My name is {first_name} {second_name}")

# calll the function
function_without_parameter()


# FUNCTION RETURNING A VALUE
# a function can return a value. If a function does not have a return statement, the value of the return type is none.

def generate_full_name():
    first_name = 'Alex'
    last_name = 'Mwangi'
    full_name = first_name + ' ' + last_name
    return full_name
print(generate_full_name())
