"""
Simulation of the Billy Goat's Gruff
file: gruff.py
author: Arthur Nunes-Harwitt
"""

from random import *
from goatsTroll import *
from cavern import *
from bridge import *

    
def welcome():
    print("Billy Goats Gruff v1.0")
    print("-------------")
    print("Welcome to the field.  Goats yearn for the berries on the hills.")

def endingCredits(troll, meadow):
    if troll.hitPoints > 0:
        print("The troll, with", troll.hitPoints,
            "hit points remaining, claims victory!")
    elif meadow.size > 0:
        print(meadow.size, "goats reach the berries and eat their fill!")
        while not emptyQueue(meadow):
            goat = front(meadow)
            dequeue(meadow)
            print(goat.name, ", with", goat.hitPoints,
                "hit points remaining, eats berries!")
        print("The goats live happily ever after!")
    print("THE END.")
    
def main():
    welcome()
    # spawn the troll!
    troll = createTroll()
    print("The troll spawns somewhere in front of the bridge with", 
        troll.hitPoints, "hit points...")
        
    # create the goats and push them into the cavern
    numGoats = int(input("How many goats? "))
    cavern = createStack()
    for id in range(1, numGoats+1):
        goat = createGoat(id)
        print("Goat", goat.name, "with", goat.hitPoints,
            "hit points and", goat.weight, "weight, enters the cavern...")
        push(cavern, goat)
        
    # get the berries!
    surviveTheCavern(troll, cavern)
    meadow = createQueue()
    if (cavern.size > 0):
        input("Hit enter to continue...")
        crossTheBridge(cavern, meadow)

    endingCredits(troll, meadow)
   
main()
