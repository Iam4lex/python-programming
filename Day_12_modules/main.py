# Import the module using the import keyword

# importing functions from a module
# - We can import many function which are inside the module

from module import my_name, total, area_of_circle


print(my_name(input("Enter the first name : "), input("Enter the second name : ")))

print(total(first_number = int(input("Enter the first number ")),
    second_number = int(input("Enter the second number "))))

print(area_of_circle(radius = int(input("Enter the radois of the circle\n: "))))