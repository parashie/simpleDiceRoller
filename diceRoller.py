import math
import random
min = 1
max = 6

#Function dice roller
def rollDice():
    #Lets user know code is running
    print("rolling a dice 1-6")
    print("rolling...")
    #Defined earlier, our minimum and maximum are 1 and 6
    print(random.randint(min, max))
    roll = input("Roll again?")
    #to be honest I think after you initally say yes itll keep going forever...
    if roll == "yes":
        rollDice()

roll = input('Hello user, would you like to roll the dice?')

while roll == "yes" or roll == "y":
    rollDice()


