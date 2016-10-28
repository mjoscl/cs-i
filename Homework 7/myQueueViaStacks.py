"""
file: myQueueViaStacks.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:
this program provides functionality for testQueueViaStacks.py for homework 7.
testQueueViaStacks imports this file which provides the helper functionality to
the queus via stacks object created which includes: enqueue, deqeue, front,
back, createQVS object, and emptyQueue.
"""


# --IMPORT STATEMENTS--
from rit_lib import *
import myStack


# --CLASS DECLARATIONS--
class QueueViaStacks(struct):
    """
    this class simulates a queue data type by using two stacks, each
    a mirror image of each other. Stack1 represents the front (head) of the
    queue and stack2 represents the back (tail) of the queue. Items will be
    added to stack2 and removed from stack1
    """
    _slots=((myStack.Stack,'stack1'),(myStack.Stack,'stack2'),(int,'size'))


# --FUNCTIONS--
def enqueue(queue, element):
    """
    This function modifies the queue and adds the element to the back (tail)
    of the queue by utilizing or altering oner or both of the internal stacks to
    ultimately 'enqueue' the queue. the enqueue is simulated by pushing an
    element to stack2
    :param queue: the queue via stacks class object
    :param type: queue
    :param element:the object value to add to the 'queue'
    :param type: object
    :return: the object that was added to the queue via stacks
    :rtype: object
    """
    if emptyQueue(queue):
        myStack.push(queue.stack1,element)
        myStack.push(queue.stack2,element)
    else:
        myStack.push(queue.stack2,element)
        temp_list=[]
        while not myStack.emptyStack(queue.stack1):
            myStack.pop(queue.stack1)
        while not myStack.emptyStack(queue.stack2):
            myStack.push(queue.stack1,myStack.top(queue.stack2))
            temp_list+=[myStack.top(queue.stack2)]
            myStack.pop(queue.stack2)
        for element in temp_list[::-1]:
            myStack.push(queue.stack2,element)
    queue.size += 1
    return element
    
    
def dequeue(queue):
    """
    This function modifies the queue and removes the element to the front (head)
    of the queue by utilizing or altering one or both of the internal stacks to
    ultimately 'dequeue' the queue. the dequeue is simulated by popping an
    element from stack1. the popped, or 'dequeue'd' element is returned
    :param queue:
    :param type: queue
    :return: the element removed from the queue via stacks
    :rtype: object
    """
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    else:
        removed_element=myStack.top(queue.stack1)
        myStack.pop(queue.stack1)
        queue.size-=1
        temp_list=[]
        while not myStack.emptyStack(queue.stack2):
            temp_list+=[myStack.top(queue.stack2)]
            myStack.pop(queue.stack2)
        for element in temp_list[::-1]:
            if element != removed_element:
                myStack.push(queue.stack2,element)
        
        
def front(queue):
    """
    this function takes the queue as a single argument and returns the
    equivalent first element to be removed, i.e., stack1 will be peeked
    :param queue: the queue via stacks class object being manipulated
    :param type: queue
    :return: the element that was a the front of the queue via stacks
    :rtype:object
    """
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    return myStack.top(queue.stack1)
    
    
def back(queue):
    """
    this function takes the queue as a single argument and returns the
    equivalent of the tail element of the queue, i.e., stack2 will be peeked
    :param queue: the queue via stacks class object being manipulated
    :param type: queue
    :return: the element that was at the back of the queue via stacks
    :rtype:object
    """
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    return myStack.top(queue.stack2)
    
    
def emptyQueue(queue):
    """
    this function performs the equivalent queue function of checking to see
    if the queue is empty or not. it returns a boolean response
    :param queue:the queue via stacks class object
    :param type: queue
    :return: True if the size of the queue via stacks is 0
    :rtype: bool
    """
    if queue.size==0:
        return True
    
    
def createQVS():
    """
    This function creates stack1 to represent the front of the queue and stack2
    which represents the back of the queue. finally the queue object is created
    and returned with all None and 0 values.
    :return: QueueViaStacks class object
    :rtype: queue
    """
    stack1=myStack.Stack(None,0)
    stack2=myStack.Stack(None,0)
    return QueueViaStacks(stack1,stack2,0)


