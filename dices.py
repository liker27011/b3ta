'''
    Dev: Marlon J. Lopes 
    Description: 
    Get player name
    Generate two random number into  two dices
    Dice one: 1-6
    Dice two: 1-6
    Print dices values
'''
import os 
from random import randint, uniform

# Functions #################################
def get_dices():
    os.system('clear')
    print("::: WELCOM TO MY PARCHIS :::")

    # print("Player name:")
    player_name = input("Player name:")
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    print(f"Dice 1: {dice1}")       # print("Dice 1: ", dice1)
    print(f"Dice 2: {dice2}")       # print("Dice 2: ", dice2)

get_dices()