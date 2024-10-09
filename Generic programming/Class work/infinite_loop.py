
## Infinite loop

print("ENter -1 to terminate")
number = 0
while number > 0:
    number = input("Enter a number to squre: ")
    number = int(number)

    number *= number

    print(number)

    