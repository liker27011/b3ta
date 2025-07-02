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
    if z == '1':
        return x + y
    if z == '2':
        return x - y
    if z == '3':
        return x * y
    if z == '4':
        if y == 0:
            return "Dato invalido (división por cero)"
        return x / y
    return "Opción inválida"

def calc2(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return "Dato invalido (división por cero)"
        return x / y
    return "Opción inválida"

def calc3(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return "Dato invalido (división por cero)"
        return x / y
    elif z == '5':
       
        results = f"""
        Suma: {x + y}
        Resta: {x - y}
        Multiplicación: {x * y}
        División: {"Dato invalido (división por cero)" if y == 0 else x / y}
        """
        return results.strip()
    else:
        return "Por favor, elija una opción del 1 al 5."

def calc4():
    os.system("cls" if os.name == "nt" else "clear")  

    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))

    print("### MENÚ PRINCIPAL ###")
    print("[1]. Sumar")
    print("[2]. Restar")
    print("[3]. Multiplicar")
    print("[4]. Dividir")
    print("[5]. Todas las operaciones")
    opt = input("::. Elija una opción: ")

    resultado = calc3(num1, num2, opt)  
    print(f"\nResultado con función 4:\n{resultado}")

calc4()