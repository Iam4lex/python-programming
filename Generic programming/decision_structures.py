
first_number = eval(input("Please enter the first number : "))
second_number = eval(input("Please enter the second number : "))

first_number = int(first_number)
second_number = int(second_number)

if first_number > second_number:
    print(f"The first number({first_number}) is greater than the second number({second_number}).")

else:
    print(f"The second number({second_number}) is greter then the first number({first_number}).")




# Program containing 2 if statements

temperature = eval(input("Please enter your temperature in degrees celcious: "))

temperature = int(temperature)
if temperature > 37 and temperature < 100:
    print("You have fever. Please go see a doctor!")

elif temperature == 37:
    print("You're healthy!")

elif temperature > 0 and temperature < 37:
    print("You have cold. Please go see a doctor!")

else:
    print("Invalid temperature!!")