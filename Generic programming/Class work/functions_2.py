
# In python, a function can return another function

def sum_and_difference(a, b):

    sum = a + b
    difference = a - b

    return sum, difference

s, d = sum_and_difference(90, 50)

print(s) # prints the sum of the numbers
print(d) # prints the difference of the numbers

