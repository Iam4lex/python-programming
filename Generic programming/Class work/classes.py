

"""
    Python classes small notes
    
    sytax
        class ClassName:
            block of code

    The self parameter method defination is required in after declaring a class name
    It is an equivalent of 'this' in Java

    Initializer method, It is an equivalent of a constructor in Java
    systax => def __init__ (self)
"""

# Example

import random

def main():

    c = Card()
    c.selectAtRandom()
    print(c)

class Card:

    def __init__(self, rank="", suit=""):

            self._rank = rank
            self._suit = suit
        
    def selectAtRandom(self):
            ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            self._rank = random.choice(ranks)
            self._suit = random.choice(["Red", "Blue", "Green", "Yellow", "Orange"])

    def __str__(self):

            return (f"{self._rank} of {self._suit}")

main()        