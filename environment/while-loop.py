# Working with Loops

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False    

while isGuessRight != True:
    guess = input("Enter a number (1-10)")
    
    if guess == number:
        print(f"You guessed {guess} which is correct. Congratulations!")
    else:
        print("Sorry you guessed {} which is incorect. Try again".format(guess))