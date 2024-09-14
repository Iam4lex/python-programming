# Program to print a square

for row in range(5):
    for column in range(5):
        print("*", end="")
    print()


# Function to print the pattern

def pattern():

    number_of_rows = int(input("Enter the number of rows "))
    number_of_columns = int(input("Enter the number of columns "))

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            print("*", end="")
        print()

# call the function
pattern()