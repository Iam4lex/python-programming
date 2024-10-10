"""
4.Write a Python program to print the number of prime numbers which are less than or equal
to a given integer.
"""

number = int(input("Enter a posive number: "))
primes = []

for num in range(2, number+1):
    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            break
    else:
        primes.append(num)
print(f"Number of prime numbers: {len(primes)}")

