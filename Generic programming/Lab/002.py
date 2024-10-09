
"""
2.	Write a Python program to print a long text, convert the 
string to a list and print all the words and their frequencies. 
"""

def words_and_frequencies(text):
    print(f"Original text: {text}")
    words_frequencies = {}

    words_list = text.split(" ")

    for word in words_list:
        word = word.strip("!.,?")
        words_frequencies[word] = words_frequencies.get(word, 0) + 1

    for word, frequence in words_frequencies.items():
        print(f"{word}: {frequence}")


text = input("Enter long text: ")
words_and_frequencies(text)

