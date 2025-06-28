#Script description
'''
1. Get 2 numbers (Float or integer)
2. Show main menu: (1). Add, (2). Sub, (3). Mul, (4). Div
3. Select an option
4. Create a function to get the result according whit de opt
Other: Clear screen

'''
import os

def calc(x, y, z):
    if(z == '1'):
        ans = x + y

    if(z == '2'):
        ans = x - y

    if(z == '3'):
        ans = x * y

    if(z == '4'):
        ans = x / y        
    
    return ans

def calc2(x, y, z):
    if(z == '1'):
        ans = x + y
    else: 
        if(z == '2'):
            ans = x - y
        else:
            if(z == '3'):
                ans = x * y
            else:
                if(z == '4'):
                    ans = x / y

    return ans

def calc(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return "¡No sea bruto! No se puede dividir por 0."
        else:
            return x / y
    else:
        return "Opción inválida. Por favor, elija una opción del 1 al 4."

#### Main ####
num1 = float(input('Press first number: '))
num2 = float(input('Press second number: '))

print("### MAIN MENU ###")
print("[1]. Add")
print("[2]. Sub")
print("[3]. Mul")
print("[4]. Div")
opt = input("::. Press any option: ")

res = calc(num1, num2, opt)
print(f"The result is: {res}")