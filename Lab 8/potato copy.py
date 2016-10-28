"""
file: potato.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:lab8

"""


# --IMPORT STATEMENTS--

import random


def remove(lst):
    prev=lst.cursor.prev
    next=lst.cursor.next
    
    if not next is None and not prev is None:
        next.prev=prev
        prev.next=next
        lst.cursor=next
    elif next==None:
        prev.next=next
        lst.cursor=next
    elif prev==None:
        next.prev=prev
        lst.cursor=next
    lst.size-=1
    

def create_list():
    return dlList(None, None, 0, None)


def append(lst, name):
    if lst.head==None:  #list is empty
        lst.head=dlNode(name,None) #this will be the only node in LL
    else:               #list is non-empty
        curr=lst.head
        while curr.next != None:
            curr=curr.next
        curr.next=dlNode(name,None)
        #(curr.next).prev=curr
        curr=curr.next
        lst.tail = curr
    lst.size+=1


def remove_player(lst,player_index):
    """
    
    :param lst:
    :param index:
    :return:
    """
      
    if player_index <= 0 or player_index>lst.size:
        raise IndexError("Player index is out of range")
    player_removed=""
    if player_index==1:
        player_removed=lst.head.data
        lst.head=lst.head.next
    elif player_index==lst.size:
        cursor = lst.head
        index = 1
        while index != player_index - 1:
            cursor = cursor.next
            index += 1
        player_removed = cursor.next.data
        cursor.next = None
        lst.tail=cursor
    else:
        cursor=lst.head
        index=1
        while index != player_index-1:
            cursor=cursor.next
            index+=1
        player_removed=cursor.next.data
        cursor.next=cursor.next.next
    lst.size-=1
    lst.cursor=None
    print("Removed:",player_removed)



def play_game(lst):
    """
    
    :param lst:
    :return:
    """
    ###1 - get random #
    #2 -Pass the potato that number (sign=direction, CW+)
    #3 - if 0, the one there loses
    #4 - the potato can be passed a maximum of 2 in one round (get a max value for the random #, get a new one)
    #5 - remove player
    #6 - give potato to next user
    #random_number=random.randint(-(2*lst.size),(2*lst.size))
    random_number = random.randint(1, (2 * lst.size))+1
    cursor=lst.head
    player_to_remove_index=0
    player_order = "The music starts (" + str(random_number) + "):"
    player_to_remove_name=""
    if random_number==1:
        player_to_remove_index=1
        player_to_remove_name=lst.head.data
        player_order=player_order + lst.head.data + "*->"
    elif random_number > 1:
        for counter in range(1,random_number+1):
            if counter == lst.size+1:
                cursor = lst.head
                player_to_remove_index=1
                player_to_remove_name=lst.head.data
                #player_order = player_order + lst.head.data + "**->"
            else:
                player_order = player_order + cursor.data + "->"
                player_to_remove_name=cursor.data
                cursor=cursor.next
                player_to_remove_index+=1
                

    #player_order = player_order + player_name + "->"
    player_order=player_order+str(player_to_remove_name)
    
    print(player_order)
    remove_player(lst,player_to_remove_index)
        
    #elif random_number < 0:
    #    for counter in range(random_number+1,1,-1):
    #        print(counter)
   
   
    
def main():
    print("Welcome to the Hot Potato Game!")
    print("Enter a file of contestants: pokemon.txt")
    print("Enter a seed number for random number generator: 10")
    file_name="pokemon.txt"
    seed_number=10
    random.seed(seed_number)
    #file_name = input("Enter a file of contestants:")
    #seed_number = input("Enter a seed number for random number generator:")
    print("Ready to Play Hot Potato. Conestants are:")
    dlList=create_list()
    for name in (open(file_name)):
        print(name.strip())
        append(dlList,name.strip())
    play_game(dlList)
    
    print(dlList)
    while not cursor==None:
        print(cursor)
        cursor=cursor.next



if __name__ == "__main__":
    """ this is a description of what the main function does """
    main()