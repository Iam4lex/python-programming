
# Fibonachi is a series of numbers where each number is the sum of the 2 proceeding numbers

a = 0
b = 1

number_of_times = input("Enter the number of times to generate the series: ")
number_of_times = int(number_of_times)

print("FIBONACHI SEIRIES")
for i in range(1,  number_of_times+1):
    c = a + b
    a = b
    b = c
    print(f" {c}", end="")
    