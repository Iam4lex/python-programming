"""4.Write a Python program to print the number of prime numbers which are less than or equal to a given integer."""

def prime(num):
    for n in range(num+1, 2):
        if n % 2 == 0:
            print(n)


prime(10)