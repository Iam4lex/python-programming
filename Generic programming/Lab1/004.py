"""
4.Write a Python program to print the number of prime numbers which are less than or equal
to a given integer.
"""

lower_number = int(input("Enter the lower number:"))
upper_number = int(input("Enter a upper number: "))

primes = []

# all_nums = [num for num in range(lower_number)]

for num in range(lower_number, upper_number+1):
    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            break
    else:
        primes.append(num)

print(primes)
print(f"Number of prime numbers: {len(primes)}")

