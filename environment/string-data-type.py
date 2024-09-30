string = "This ia a string"

print(string)

print(type(string))

print(str(string) + " is a data type of " + str(type(string)))

# string concantenation
firstString = "My name is "
secondString = "Alex"
thirdString = firstString + secondString

print(thirdString)

# working with input strings
name = input("What is your name?")
print(name)

# Formatting output strings 

color = input("What is your favorite color? ")
print("My favorite color is " + color)

animal = input("What is your favorite animal? ")
print("My favorite animal is " + animal)

#  string interpolation

print("My favorite color is {} and animal is {}".format(color, animal))