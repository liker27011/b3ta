import os

os.system("clear")

li = int(input("Ingrese el número de inicio (li): "))
ls = int(input("Ingrese el número de fin (ls): "))

i = li
if li <= ls:
    while i <= ls:
        print(i)
        i += 1
else:
    while i >= ls:
        print(i)
        i -= 1

