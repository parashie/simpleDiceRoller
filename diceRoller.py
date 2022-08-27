import math
import random
min = 1
max = 6


def rollDice():
    print("rolling a dice 1-6")
    print("rolling...")
    print(random.randint(min, max))
    roll = input("Roll again?")
    if roll == "yes":
        rollDice()

roll = input('Hello user, would you like to roll the dice?')

while roll == "yes" or roll == "y":
    rollDice()


