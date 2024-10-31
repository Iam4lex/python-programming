
''' 
1.	Write a Python function that takes a sequence of numbers and 
determines whether all the numbers are different from each other. 
'''

# Define a function
def sequence_of_numbers():
    list_of_numbers = [1, 2, 3, 4, 5, 5]

    if len(list_of_numbers) == set(list_of_numbers):
        print("Numbers are unique")
    
    else:
        print("Numbers are not unique")

# Call the function
sequence_of_numbers()