# Squre patter using a function

# define the function

def squre_pattern():

    number_of_rows = int(input("Enter the number of rows: "))
    number_of_columns = int(input("Enter the number of columns: "))

    for row in range (number_of_rows):
        for column in range(number_of_columns):
            print("*", end=" ")
        print()

# call the function
squre_pattern()