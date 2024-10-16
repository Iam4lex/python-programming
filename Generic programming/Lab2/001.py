
integer = int(input("Enter an integer: "))

if integer == 0:
    print("The integer is 0.")
elif integer < 0:
    print("Negative integer are not allowed.")
else:
    binary_str = ""
    original_int = integer

    while integer > 0:
        remainder = integer % 2
        binary_str = str(remainder) + binary_str
        integer = integer // 2
    print(f"Binary representation of {original_int} is: {binary_str}")

    # Back to integer
    decimal_value = 0
    for key, value in enumerate(reversed(binary_str)):
        if value == "1":
            decimal_value += 2 ** key
    print(f"Converted back to integer: {decimal_value}")
