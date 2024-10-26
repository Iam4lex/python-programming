
# finding the squre of even numbers using list cpmrehension
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square_of_even():
    for i in my_list:
        if i % 2 == 0:
            print(i**2)

square_of_even()

# alternatively

lst = [i**2 for i in my_list if i % 2 == 0]
print(lst)



def total(w, x, y=10, z=20):
    return (w**x) + y + z

print(total(w=3, x=2))


# Custom sorting

def main():
    list1 = ["Alex", "Mwangi", "Mungai", "Dorcas", "Kamau", "Mary"]

    print(list1.sort(key=len))

main()

# lambda expressions

add_numbers = lambda first_number, second_number: first_number + second_number

print(add_numbers(10, 10))


marks = [90, 79, 98, 87, 98, 99, 78]

marks.sort()

marks.reverse()

print(marks)


scores = sorted(marks)

