
try:
    number = input("Enter a number: ")
    number = int(number)

    number += 1
    print(number)

except Exception as e:
    print("Something went wrong")
    print(e)


# Example

def main():
    try:
        file_name = input("Enter the name of the file: ")
        infile = open(file_name, "r")

        num = float(infile.readline()) 
        print(1 / num)

    except FileNotFoundError as exc1:
        print("Something went wrong")
        print(exc1)

    except TypeError as exc2:
        print(exc2)

# call the function
main()


def main():

    phonetical_alphabet = {
        'a':'alpha',
        'b':'beta',
        'c':'charie'
    }

    while True:
        try:
            letter  = input("Enter a, b or c: ")
            print(phonetical_alphabet[letter])
            break
        
        except Exception as e:
            print(f"{letter} not accepted. Please enter a, b or c")
            print(e)

main()