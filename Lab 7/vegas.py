"""
file: vegas.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:
lab 7 - this card game simulation first prompts the user for the number of cards to play
in a deck as well as the number of rounds to play. the game is then simulated
followed by a summary of the money spent and earned and relative statistics.
"""


# --IMPORT STATEMENTS--
from rit_lib import *
import myStack
import myQueue
import random


# --FUNCTIONS--
def get_deck(number_of_cards):
    """
    this function creates the queue object called deck and populates the deck
    with the number of cards specified, in order from 1 to number_of_cards.
    lastly, the deck queue is returned.
    :param number_of_cards: the maximum number of cards to play
    :param type: int
    :return: the deck queue containing the unshuffled deck
    :rtype: queue
    """
    deck=myQueue.createQueue()
    for card_number in range(number_of_cards):
        myQueue.enqueue(deck,(card_number+1))
    return deck
    
    
def shuffle(deck):
    """
    this function takes the unshuffled, ordered deck and randomly shuffles it.
    this is done by randomly choosing a number between 1-100 and removing the
    top card from the queue and putting it on the bottom.
    :param deck: this is the deck to be shuffled
    :param type:queue
    """
    for shuffle_count in range(1,random.randint(1,100)):
        myQueue.enqueue(deck,myQueue.front(deck))
        myQueue.dequeue(deck)
    

def decide_card_destination(deck, discard1, discard2, vp):
    """
    this function takes in the shuffled deck as a queue, the two discard stacks,
    and the victory pile stack. the top card is removed the the decision process
    starts. the algorithm is as follows (- indicates level on decission tree):
    -Q: is this the next card on the victory pile?
    -A: card is the next for the victory pile
        -add the card on the victory pile (push to vp stack)
    -A: card is not the next for the victory pile
    --Q:which discard pile should this card go on?
    --A:if both discard piles are empty, push to discard1 stack
    --A:if discard pile 1 has cards, but discard pile 2 is empty, push to 2
    --A:if both discard piles have cards, decide which is best for card
    ---Q:which discard pile should card go on, since both have cards already?
    ---A:if the card value > than both discard pile top cards OR less than both
         discard pile top cards, push card to the discard pile with the
         smallest difference between it and the card
    ---A:if the card value is in between the values of the top card on the
         two discard piles, push the card to the discard stack that has the
         larger of the two numbers, allowing for the card with the smaller
         value to be accessible
    :param card: the value of the dealt card from the deck queue
    :param type: int
    :param discard1: the discard 1 pile
    :param type:stack
    :param discard2:the discard 2 pile
    :param type:stack
    :param vp: the victory pile
    :param type:stack
    """
    card=myQueue.front(deck)
    myQueue.dequeue(deck)
    if card==(vp.size+1):
        myStack.push(vp,card)
    else:
        if discard1.size==0 and discard2.size==0:
            myStack.push(discard1,card)
        elif discard1.size>0 and discard2.size==0:
            myStack.push(discard2,card)
        elif discard1.size>0 and discard2.size>0:
            if (card>myStack.top(discard1) and card>myStack.top(discard2)) or (card<myStack.top(discard1) and card<myStack.top(discard2)):
                difference1=abs(card-myStack.top(discard1))
                difference2=abs(card-myStack.top(discard2))
                if (difference1<difference2) or (difference1==difference2):
                    myStack.push(discard1,card)
                elif difference1>difference2:
                    myStack.push(discard2,card)
            elif (card > myStack.top(discard1) and card < myStack.top(discard2)) or (card < myStack.top(discard1) and card > myStack.top(discard2)):
                if myStack.top(discard1) > myStack.top(discard2):
                    myStack.push(discard1,card)
                else:
                    myStack.push(discard2,card)
    

def final_vp_check(number_of_cards,discard1,discard2,vp):
    """
    this function is called once the deck is exhausted. it examines the two
    top cards on each of the discard piles to see if they are the next in
    sequence for the victory pile. This action is repeated a number of times
    equal to twice the number of cards to ensure that both the discard1 and
    discard2 decisions have been evaluated as many times as needed
    :param number_of_cards:the number of cards the deck started with
    :param type: int
    :param discard1:this is the discard1 pile
    :param type: stack
    :param discard2:this is the discard2 pile
    :param type: stack
    :param vp:this is the victory pile
    :param type: stack
    """
    number_of_changes=0
    for counter in range(2*number_of_cards):
        if myStack.emptyStack(discard1) == False:
            if (myStack.top(discard1) == (myStack.top(vp) + 1)):
                number_of_changes+=1
                print("Moving",myStack.top(discard1),"to vp with card",myStack.top(vp))
                myStack.push(vp, myStack.top(discard1))
                myStack.pop(discard1)
        if myStack.emptyStack(discard2) == False:
            if (myStack.top(discard2) == (myStack.top(vp) + 1)):
                number_of_changes += 1
                print("Moving", myStack.top(discard2), "to vp with card",myStack.top(vp))
                myStack.push(vp, myStack.top(discard2))
                myStack.pop(discard2)


def run_game_sim(number_of_cards,number_of_rounds):
    """
    this function controls gameplay. first, it initializes all the variables
    then, it iterates through each round. each round consists of resetting
    the round variables and shuffling the deck and deciding where the top
    card of the deck queue goes.that shuffling and deciding is a loop until
    the deck is exhausted, in which case the round statistics are completed
    finally, the game statistics are totaled and returned to the user.
    :param number_of_cards: the maximum number of cards for the deck
    :param type:int
    :param number_of_rounds: the maximum number of iterations to play
    :param type: int
    """
    total_vp_size=0
    max_vp_size=0
    min_vp_size=0
    round_money_spent=0
    total_money_spent=0
    total_money_earned=0
    for round_count in range(1,(number_of_rounds+1)):
        deck=get_deck(number_of_cards)
        discard1 = myStack.Stack(None,0)
        discard2 = myStack.Stack(None,0)
        vp=myStack.Stack(None,0)
        while deck.size > 0:
            shuffle(deck)
            decide_card_destination(deck,discard1, discard2, vp)
        final_vp_check(number_of_cards,discard1,discard2,vp)
        round_money_spent+=5
        total_money_earned+=vp.size
        total_money_spent += round_money_spent
        total_vp_size+=vp.size

        if vp.size > max_vp_size:
            max_vp_size=vp.size
        if vp.size < min_vp_size:
            min_vp_size=vp.size
        total_vp_size += vp.size
    print("Average victory pile size:", float(total_vp_size/number_of_rounds))
    print("Max victory pile size:", max_vp_size)
    print("Min victory pile size:", min_vp_size)
    print("Total amount of money spent $",float(5*number_of_rounds))
    print("Total money won: $", float(total_money_earned))
    print("Gross amount of money earned playing",number_of_rounds,"games $",float(total_money_earned-(5*number_of_rounds)))


def main():
    """
    this main function prompts and accepts the inputs and initiates gameplay
    """
    number_of_cards = int(input("Enter the number of cards to use:"))
    number_of_rounds = int(input("Enter the number of games to simulate:"))
    run_game_sim(number_of_cards,number_of_rounds)


main()