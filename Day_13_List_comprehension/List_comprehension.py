
# You can change a string of characters into a list in different ways.
# Example

my_name = "Alex Mwangi"

change_to_list = list(my_name) # Chnage the string my_name to list

print("My name is ", my_name)
print("The list is ", change_to_list)

# Another way to convert the list is : List comprehension

full_name = "Alex Mwangi"

the_list = [i for i in full_name]

print("The same list is ",the_list)


list_of_numbers = [i for i in range(10)] # Numbers between 0 and 10 ie. 1-9

print(list_of_numbers) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# You can also print the squres of the list_of_numbers

squre_of_numbers = [i * i for i in range(10)]

print(squre_of_numbers)


# You can also print list of tuples

list_of_tuples = [(i , i * i) for i in range(10)]

print(list_of_tuples)