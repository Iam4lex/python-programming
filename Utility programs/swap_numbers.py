# A program to swap numbers using the third variable

first_number = input("Enter the first number: ") # 10

second_number = input("Enter the second number: ") # 20

first_number = int(first_number)
second_number = int(second_number)


print("The first number before swap is ", first_number)
print("The second number before swap is ", second_number)

temp = first_number + second_number # 30

first_number = temp - first_number # 20

second_number = temp - second_number


print("The first number after swap is ", first_number)
print("The second number after swap is ", second_number)

# A program to swap numbers without using the third variable

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("The first number after  second swap is ", first_number)
print("The second number after second swap is ", second_number)