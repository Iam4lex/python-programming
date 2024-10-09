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

def word_letters(text):
    words_frequency = {}
    words = text.split(" ")
    frequent_word = []

    for word in words:
        word = word.strip("!?.,")
        words_frequency[word] =   words_frequency.get(word, 0) + 1

    for key, value in words_frequency.items():
        frequent_word.append(value)
        if value == max(frequent_word):
            print(key)
text = input("Enter text: ")
word_letters(text)
