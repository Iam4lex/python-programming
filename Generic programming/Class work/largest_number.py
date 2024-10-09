
# A program to find the largest number

first_number  = input("Enter the first number: ")
second_number = int(input("Enter the second number: "))

first_number = int(first_number)

if first_number > second_number:
    print(first_number, " is greater than ", second_number)

elif first_number == second_number:
    print(first_number, " is equal to ", second_number)

else:
    print(second_number, " is greater than ", first_number)
