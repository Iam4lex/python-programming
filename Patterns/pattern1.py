
"""
    Python program to print the following perttern
    * * * * * * * * * 
    * * * * * * * * *
    * * * * * * * * *
    * * * * * * * * *
    * * * * * * * * * 
    * * * * * * * * *
    * * * * * * * * * 
    * * * * * * * * * 
    * * * * * * * * *
"""

for column in range(1, 10):
    for row in range(1, 10):
        print("*", end=" ")
    print()