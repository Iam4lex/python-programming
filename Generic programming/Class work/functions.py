

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


## pay

def pay(wage, hours):

    if hours <= 40:
        amount = wage * hours
    
    else:
        amount = (wage * 40) + ((1.5) * wage * (hours - 40))

        return amount
    
hourly_wage = eval(input("Enter the hourly wage: "))
hours_worked =  eval(input("Enter the number of hours worked: "))
print(pay(hourly_wage, hours_worked))