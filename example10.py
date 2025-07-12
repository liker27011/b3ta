from random import randint

i = 1
respuesta = "s"

while respuesta == "s":
    print(f"\nLanzamiento {i}")
    print("Dado 1:", randint(1, 6))
    print("Dado 2:", randint(1, 6))

    respuesta = input("¿Quieres volver a tirar los dados? (s/n): ")
    while respuesta not in ("s", "n"):
        print(" Solo puedes ingresar 's' (sí) o 'n' (no).")
        respuesta = input("¿Quieres volver a tirar los dados? (s/n): ")

    i += 1

print("\n Gracias por jugar. ¡Hasta la próxima!")
