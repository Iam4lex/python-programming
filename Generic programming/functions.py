

# Python functions
# A function has a function name, function body and parameters

def my_function(radius):

    radius = int(radius)

    area  = (22 * radius * radius) / 7

    return area

print(my_function(radius=input("Enter the radius of the circle: ")))


# example 2

def first_name(full_name):
    ## Extract the first_name from the given full name

    first_space = full_name.index(" ")
    given_name = full_name[:first_space]
    return given_name

print(first_name(full_name = input("Please enter your full name: ")))
