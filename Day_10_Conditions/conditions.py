# syntax
# if condition:
#    code
# elif condition:
#    code
# else:
#    code

# example

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed