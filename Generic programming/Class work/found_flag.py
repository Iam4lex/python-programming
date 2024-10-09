# Find integers by division
list1 = ['one', 23, 17.3,'two', 22]
i = 0

foundFlag = False
while i < len(list1):
    x = list1[i]
    i += 1
    if not isinstance(x, int):
        continue # skip to next item in list

    if x  % 11 == 0:
        foundFlag = True
        print(f"{x} is the first in that is divisible by 11.")
        break

    if not foundFlag:
        print("There is no int in the list that is divisiblke by 11.")