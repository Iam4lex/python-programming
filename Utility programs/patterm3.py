# A program to print  the following structure

# Enter the number of rows 6
# Enter the number of columns 7
# 1234567
# 1234567
# 1234567
# 1234567
# 1234567
# 1234567

number_of_rows = int(input("Enter the number of rows "))
number_of_columns = int(input("Enter the number of columns "))

for row in range(1, number_of_rows+1):
    for column in range(1, number_of_columns+1):
        print(column, end="")
    print()


# A function to print thr program

def pattern2():
    number_of_rows = int(input("Enter the number of rows "))
    number_of_columns = int(input("Enter the number of columns "))

    for row in range(1, number_of_rows+1):
        for column in range(1, number_of_columns+1):
            print(column, end="")
        print()

# call the function
pattern2()
