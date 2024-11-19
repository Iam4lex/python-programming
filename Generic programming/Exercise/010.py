x = 10
y = 5
z = 2

smallest = x  # Assume x is the smallest initially
if y < smallest:
    smallest = y
if z < smallest:
    smallest = z

print(smallest)  # Output will be 2, as z is the smallest
