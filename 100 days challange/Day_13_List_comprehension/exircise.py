#1. Exercises: Day 13
# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [i for i in numbers if i <= 0]

print(filtered_numbers)

#2. Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten_numbers = [number for i in list_of_lists for number in i]

list_of_numbers = [number for i in flatten_numbers for number in i]

print(list_of_numbers)


numbers = [10, 20, 30, 40, 50]

print(f"{[ i for i in numbers]}")