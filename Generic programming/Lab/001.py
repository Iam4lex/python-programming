
''' 
1.	Write a Python function that takes a sequence of numbers and 
determines whether all the numbers are different from each other. 
'''


def is_all_number_unique(numbers):
    print(len(numbers) == len(set(numbers)))


sequence = [1, 2, 3, 4, 5, 2]

is_all_number_unique(sequence)