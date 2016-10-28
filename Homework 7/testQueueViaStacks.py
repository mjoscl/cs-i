"""
file: testQueueViaStacks.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: this is the test function that tests each of the helper functions
imported from myQueueViaStacks module
"""

# --IMPORT STATEMENTS--
from myQueueViaStacks import *


def main():
    """
    This function attempts to test all the functionality of the helper
    functions imported from myQueueViaStacks module. the helper functions tested
    include creating a queue via stacks, accessing the empty and populated head
    and tail elements of the queue via stacks, enqueu'ing and dequeue'ing
    values to and from the queue via stacks class
    :return: None
    :rtype: NoneType
    """
    # begin with an empty queue
    queueCh=createQVS()
    print("Creating empty queue...")
    print("Queue empty?", True == emptyQueue(queueCh))
    print("Queue size is 0?", 0 == queueCh.size)
    print()
    
    
    # add first element
    print("enqueue A...")
    enqueue(queueCh, 'A')
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 1?", 1 == queueCh.size)
    print("front is A?", 'A' == front(queueCh))
    print("back is A?", 'A' == back(queueCh))
    print()
    
    # add second element
    print("enqueue B...")
    enqueue(queueCh, 'B')
    print("front is A?", 'A' == front(queueCh))
    print("back is B?", 'B' == back(queueCh))
    print()
    
    
    # add third element
    print("enqueue C...")
    enqueue(queueCh, 'C')
    print("Queue size is 3?", 3 == queueCh.size)
    print("front is A?", 'A' == front(queueCh))
    print("back is C?", 'C' == back(queueCh))
    print()
    
    
    # dequeue top element, C > !!!!ERROR!!! Should read A, not C (FIFO!!)
    print("dequeue...")
    dequeue(queueCh)
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 2?", 2 == queueCh.size)
    print("front is B?", 'B' == front(queueCh))
    print("back is C?", 'C' == back(queueCh))
    print()


    # add fourth element
    print("enqueue D...")
    enqueue(queueCh, 'D')
    print("front is B?", 'B' == front(queueCh))
    print("back is D?", 'D' == back(queueCh))
    print()


    # add fifth element
    print("enqueue E...")
    enqueue(queueCh, 'E')
    print("front is B?", 'B' == front(queueCh))
    print("back is E?", 'E' == back(queueCh))
    print()
    
    # Empty the queue
    print("Emptying the queue...")
    while not emptyQueue(queueCh):
        print("Front of queue:", front(queueCh))
        print("Back of queue:", back(queueCh))
        print("dequeue...")
        dequeue(queueCh)
    
    
main()
