
"""
7.Given a list of numbers and a number k, write a Python program to check whether 
the sum of any two numbers from the list is equal to k or not.  
For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
Sample Input:
([12, 5, 0, 5], 10)
([20, 20, 4, 5], 40)
([1, -1], 0)
([1, 1, 0], 0)
Sample Output:
True
True
True
False

"""
numbers = ([12, 5, -2, 0], 10)

number, k = numbers
seen = set()

for num in number:
    if k - num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)
    
