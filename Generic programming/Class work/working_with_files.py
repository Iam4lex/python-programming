

# working with files

listvar = []

infile = open(r"C:\Users\alexm\Desktop\Python programms\Generic programming\Class work\functions.py", 'r')

for line in infile:
    listvar.append(line.rstrip())

print(listvar)

