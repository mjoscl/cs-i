"""
Simulation of the cavern battle between goats and the troll.
file: cavern.py
author: Arthur Nunes-Harwitt
"""

from myStack import *
from random import *

def getTrollDamage():
    return randint(100, 200)
    
def getGoatDamage():
    return randint(0, 100)

def surviveTheCavern(troll, cavern):
    """cavern (stack) is updated to contain surviving goats, if any"""
    
    print("STAGE 1: BATTLE WITH THE TROLL...")
        
    print("The troll blocks the cavern exit!")
    print("The goats must fight their way out in order to survive...")
    while not emptyStack(cavern) and troll.hitPoints > 0:
        goat = top(cavern)
        pop(cavern)
        print(goat.name, "prepares to do battle with the troll...")
        while troll.hitPoints > 0 and goat.hitPoints > 0:
            # goat strikes damage first
            print("\tTroll hit points:", troll.hitPoints, 
                ",", goat.name, "hit points:", goat.hitPoints)
            dmgToTroll = getGoatDamage()
            troll.hitPoints -= dmgToTroll
            print("\t" + goat.name, "does", dmgToTroll, "damage to troll")
            if (troll.hitPoints > 0):
                dmgToGoat = getTrollDamage()
                goat.hitPoints -= dmgToGoat 
                print("\tTroll does", dmgToGoat, "damage to", goat.name)
                
        if troll.hitPoints <= 0:
            print(goat.name, "has defeated the troll!")
            # put this goat back on the stack
            push(cavern, goat)
        else:
            print(goat.name, "has fallen!")
                
    # did any goats survive?
    print(cavern.size, "goat/s survived the dark cavern...")
