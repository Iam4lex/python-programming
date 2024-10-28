
# a program to check all prime numbers from 1 - a given number

number = int(input("Please enter a number: ")) # primpt the user to enter a number

counter = 0
primes = []

for num in range(1, number+1):
    for i in range(1, num+1):
        if i % num == 0:
            counter += 1

if counter == 2:
    primes.append(num)


print(primes)