"""
Nodes
file: dlList.py
author: michael j o'connor
"""

from dlNode import *

class dlList(struct):
    """
    this class defines the doubly-linked list
    """
    _slots = (((dlNode, NoneType),'head'),
              ((dlNode, NoneType),'tail'),
              (int,'size'),
              ((dlNode, NoneType),'cursor'))
    
def create_list():
    """
    This function returns an empty list with all list slots set to empty
    :return: the empty list
    """
    return dlList(None, None, 0, None)

def append(lst, name):
    """
    this function is called to add new nodes to the list passed as a parameter
    :param lst: the list to add the name to
    :param name: the data for the new node
    :return: None
    """
    new_node = dlNode(name, False, None, None)
    if lst.head == None:
        lst.head = new_node
        lst.tail = new_node
    else:
        new_node.prev=lst.tail
        new_node.next=None
        lst.tail.next=new_node
        lst.tail=new_node
    lst.size += 1

