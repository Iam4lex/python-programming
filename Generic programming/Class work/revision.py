

my_string = "Hello world, My name is Alex"

new_string = my_string.split(" ")

words = []

for word in new_string:
    word.strip(",.?!")
    words.append(word)

print(", ".join(words))


print("I love python"[10])

# Using the find method

print(my_string.find("name"))
print(my_string.find("H"))
print(my_string.rfind("16"))


# Negative indeces
python = "Python"

print(python)

print(python[-5:4])
print(python[-5:-2])

# String concantenation

print("Hello" + " World")
print("ha" * 3)

greet = "Hellllo"

print(greet.count("l"))


# Relational operators

print(10<10.5)

# print(3 < "10") Values of different types cannot be compared

print("Dog" > "dog")

print("fun" in "refunded")

