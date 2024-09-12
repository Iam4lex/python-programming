# You can create a module using any name but save it with a .py extension

# Lets create a function inside the module which we can access in the main program

# first function
def my_name(first_name, second_name): # define a function called my_name

    # first_name = input("Enter the first name : ")
    # second_name = input("Enter the second name : ")

    return first_name, second_name

# second function
def total(first_number, second_number):
    
    sum_of_numbers = first_number + second_number

    return sum_of_numbers

def area_of_circle(radius):
    
    area = ( 22 * radius * radius ) / 7

    return area


# USING BUILT IN FUNCTIONS

# Built in functions include sys, math, os, etc

# example

import os

# os.mkdir("C:\\Users\\alexm\Desktop\\100-days-of-code\\Python_Programming") # make the directory

# os.chdir() # Chnage the directory



from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
# print(math.log10(100))    # 2


# we an also import all modules using the *

from math import *

print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
# print(math.log10(100))    # 2
