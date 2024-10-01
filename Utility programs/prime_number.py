
# Program to check if a number is prime or not

count = 0

number = input("Please enter a positive integer: ")
number = int(number)

for i in range(1, (number+1)):
    if number % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not prime")