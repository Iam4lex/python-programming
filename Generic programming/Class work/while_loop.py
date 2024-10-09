
# While loop

# syntax 
# while conditon:
    # indented blovk of statements

# example
num = 1
while num <= 5:
    print(f"{num}: hello world")
    num += 1


# Movie quotations
print("This program displays a famours movie quotation.")
responses = ('1', '2', '3')
response = '0'

while response not in responses:
    response = input("Enter 1, 2 or 3: ")
    if response == '1':
        print('Plastics.')
    elif response == '2':
        print('Rosenud.')
    elif response == '3':
        print("That's all folks.")


# example 3
# Find max, min and average of sequence of numbers.

count = 0
total = 0

print("Enter -1 to terminate entering numbers.")
num = eval(input("Enter a non negative number: "))

min = num
max = num
while num != -1:
    count += 1
    total += num
    if num < min:
        min = num
    if num > max:
        max = num
    num = eval(input("Enter non negative number: "))
    if count > 0:
        print(f"Minimum: {min}")
        print(f"Maximum: {max}")
        print(f"Average: {total / count}")


# Example 4
list1 = []

print("Enter -1 to terminate entering numbers.")
num = eval(input("Enter a non negative number: "))

while num != -1:
    list1.append(num)
    num = eval(input("Enter a non negative number: "))

if len(list1) > 0:
    list1.sort()
    print(f"Minimum: {list1[0]}")
    print(f"Maximum: {list1[-1]}")
    print(f"Sum: {sum[list1]}")

# break statement is used to terminate a loop
# continue statement is used to return the next aliteration of the loop

