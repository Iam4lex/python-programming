import random
import os

number = random.randint(1, 10)
guese = input("Enter a gues between 1 and 10: ")

guese = int(guese)

if guese == number:
    print("You won!!")

else:
    print(f"You loose, The number is {number}")