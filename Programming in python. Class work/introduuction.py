
# print function
# abs function
# int function
# round function - round off numbers round(2.345,2) -> round the number to 2 decimal places
# Example

a = 2
b = 3

print(abs(1 - (4 * b))) # prints 11

# Arguments assignments
# example

counter = 0
counter = counter + 1
counter += 1 # same thing


totoalInches = 41
feet = totoalInches // 12
inches = totoalInches % 12
print(feet, inches)


# Syntax errors
# Run time erros

# print( 5 / 0) # Will produce a runtime error

# Logic erros
# Numeric objects in memory
n = 5
n = 7

print(n)

#    WEEK 2
# Lists and Tuples
# example of a list
# systax => list_name = ['list']

list_of_fluits = ['Mango', 'Apple', "Avocado", "Tomato"]
print("The list of fluits is ", list_of_fluits)

# Reverse the list
list_of_fluits.reverse()

print("The reversed list is ",list_of_fluits )

# -  The list object
## Calculate the average of grade. Ypu can sort a list.

grade = [] # create an empty list

num = float(input("Enter the first grade: "))
grade.append(num)
num = float(input("Enter the second grade: "))
grade.append(num)
num = float(input("Enter the third grade: "))
grade.append(num)
num = float(input("Enter the forth grade: "))
grade.append(num)
num = float(input("Enter the fith grade: "))
grade.append(num)

minimum_grade = min(grade)
grade.remove(minimum_grade)
minimum_grade = min(grade)
grade.remove(minimum_grade)

average = sum(grade) / len(grade)
print("Average grade is {0:.2f}".format(average))

#           SLICES
# The plit and join metthods
# The tuple objects. You can not sort a tuple.


#example of a tuple

_tuple_ = 5, 7, 6, 2

print(_tuple_)
print(len(_tuple_), max(_tuple_))


