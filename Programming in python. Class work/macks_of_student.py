
# A function to receive the name, reg no, and marks of student. Calculate the sum, average, and grade of the student.

def student_marks():

    name_of_student = input("Please enter the marks of the student: ")
    reg_number = input("Please enter the reg number of the student: ")

    coursers = ['CSC311','CSC312','CSC313','CSC314','CSC315','CSC316','CSC317','CSC318']
    for i in coursers:
        marks = []
        mark = int(input(f"Please enter the mark of {i}: "))
        marks.append(mark)

    total = sum(marks)

    print(total)

# call the function
student_marks()