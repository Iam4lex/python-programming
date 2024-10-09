"""
5.	Write a Python program that accepts six numbers as input and sorts them in descending order. 
Input:
Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000). The six numbers are separated by a space.
Input six integers:
15 30 25 14 35 40
After sorting the said integers:
40 35 30 25 15 14

"""

def sort_desceinding(numbers):
    list_of_numbers = numbers.split(" ")
    list_of_numbers = [int(n) for n in list_of_numbers]

    for number in list_of_numbers:
        if number not in range(100000):
            print("Numbers must be within the range: -100000 to 100000")
            return
        else:
            list_of_numbers.sort(reverse=True)

    print(", ".join([str(n) for n in list_of_numbers]))


numbers = input("Enter six numbers: ")
sort_desceinding(numbers)