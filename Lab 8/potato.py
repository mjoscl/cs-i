"""
file: potato.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:lab8
This program simulates a game of hot potato using pokemon characters pulled
from a text file. The program uses a circular doubly-linked list to allow
for the passing of the 'hot potato' in either direction, based on a random
number generated prior to each round. The winner is declared when all but
one of the characters remain.
"""

import random
from dlList import *


def play_game(lst):
    """
    this function controls gameplay by iterating through the number of rounds
    and calling the perform_round function for each. the perform_round
    function returns the player to be removed for that round which is also
    called from this function.
    :param lst:the list of pokemon players in a circular, doubly-linked list
    :return: None
    """
    number_of_rounds=lst.size-1
    for round in range(1,number_of_rounds+1):
        number_of_passes=random.randint(-(2*lst.size),(2*lst.size))
        remove_player(lst, perform_round(lst,number_of_passes))
    cursor=lst.head
    print(cursor.data,"is the winner!")
        
        
def perform_round(lst,number_of_passes):
    """
    this function is called from the play_game function and controls the
    activities of one round. each round, the player whose turn it is,
    diesignated by the boolean turn slot, passes the potato in the
    designated random direction the number of times (passed parameter)
    whichever player is 'holding' the potato, i.e., cursor is on, will be
    returned for removal
    :param lst: the list of pokemon players in a circular, doubly-linked list
    :param number_of_passes: this is the number of exchanges that occur
    :return: the node data for the player node to be removed
    """
    cursor=lst.head
    while cursor.turn != True:
        cursor=cursor.next
    cursor.turn=False
    round_string = "The music starts (" + str(number_of_passes) + "):"
    for turn in range(0,abs(number_of_passes)):
        round_string = str(round_string) + cursor.data + "->"
        if number_of_passes>0:
            cursor=cursor.next
        else:
            cursor=cursor.prev
    round_string = round_string + cursor.data + " is stuck holding the potato!"
    cursor.next.next.turn = True
    print(round_string)
    return cursor.data

            
def remove_player(lst,player):
    """
    this function is called from the play_game function and it removes the
    player who was 'stuck with the potato' at the end of each round. it
    ensures that head and tail references remain intact and decrement the
    list accordingly
    :param lst: the list of pokemon players in a circular, doubly-linked list
    :param player: the player to be removed
    :return: None
    """
    print("Removing",player)
    cursor=lst.head
    while cursor.data!=player:
        cursor=cursor.next
    if cursor==lst.head:
        cursor.next.prev=lst.tail
        cursor.prev.next=cursor.next
        lst.head=cursor.next
    if cursor==lst.tail:
        cursor.next.prev=cursor.prev
        cursor.prev.next=lst.head
        lst.tail=cursor.prev
    cursor.prev.next=cursor.next
    cursor.next.prev=cursor.prev
    lst.size-=1
    
    
if __name__ == "__main__":
    """
    this main function collects the user information, populates the list
    based on the player names pulled from the file and calls the play_game
    function
    """
    print("Welcome to the Hot Potato Game!")
    file_name = input("Enter a file of contestants:")
    seed_number = input("Enter a seed number for random number generator:")
    print("Ready to Play Hot Potato. Contestants are:")
    dlList = create_list()
    for name in (open(file_name)):
        append(dlList, name.strip())
    cursor=dlList.head
    intCounter=0
    player_list=""
    number_of_commas=dlList.size-1
    while cursor is not None:
        player_list=player_list+cursor.data
        if number_of_commas>0:
            player_list=player_list+", "
        number_of_commas-=1
        cursor=cursor.next
        intCounter+=1
    print(player_list)
    dlList.head.turn=True
    #Connect the head and tail to make this dlList circular
    dlList.head.prev=dlList.tail
    dlList.tail.next=dlList.head
    play_game(dlList)
    