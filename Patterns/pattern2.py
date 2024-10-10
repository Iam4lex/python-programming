

"""
    Python program to print the following pertern
    1 1 1 1 1 1 1 1 1 
    2 2 2 2 2 2 2 2 2
    3 3 3 3 3 3 3 3 3 
    4 4 4 4 4 4 4 4 4 
    5 5 5 5 5 5 5 5 5
    6 6 6 6 6 6 6 6 6
    7 7 7 7 7 7 7 7 7
    8 8 8 8 8 8 8 8 8 
    9 9 9 9 9 9 9 9 9
"""

for column in range(1, 10):
    for row in range(1, 10):
        print(column, end=" ")
    print()