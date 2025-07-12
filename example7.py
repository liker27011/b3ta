import os
from random import randint

lan =int(input("cuantas veces debes lanzar los dados"))
i = 1 
while i <= lan :
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f"lanzamiento: {i}")
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print("\n")

    i +=1
    

    