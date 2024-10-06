
# Number gausing game

import os
import random

number = 10
number = random.randint(1, 10)

guess = input("Please enter a guess number (1-10): ")
guess = int(guess)

if number == guess:
    print("You won !")

else:
    os.remove(r"C:\Users\alexm\Desktop\Python programming\Utility programs\passwords.txt")
    print("You loose. One file deleted!")
    print(f"The corect answer is {number}")