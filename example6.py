import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")

    if dado1 % 2 == 0 and dado2 % 2 == 0:
        print("YOU WIN")
    else:
        print("YOU LOSE")


lanzar_dados()