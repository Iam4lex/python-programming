"""
6.Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. 
The first one is the word which occurs most frequently in the text. 
The second one is the word which has the maximum number of letters.  
Note: A word is a sequence of letters which is separated by the spaces.
Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation.

"""

text = input("Enter text: ")
if len(text) > 1000:
    print("The number of letters in the text must be less than or equal to 1000.")
else:
    frequency = {}
    words = text.split(" ")

    for word in words:
        word = word.strip("!?.,")
        frequency[word] =   frequency.get(word, 0) + 1
    frequently_word = max(frequency, key=frequency.get)
    long_word = max(frequency, key=len)
    print(frequently_word, long_word)