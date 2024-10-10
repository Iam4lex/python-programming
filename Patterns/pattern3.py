
"""
    Python program to print the following pertern
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10 
"""

for column in range(1, 10+1):
    for row in range(1, 10+1):
        print(row, end=" ")
    print()