
from rit_lib import *

class Node(struct):
    _slots=((object,'item'),((NoneType,'Node'),'next'))
    

def empty_stack(stack):
    return stack.top==None

def push(stack,item):
    new_top=Node(item,stack.top)
    stack.top=new_top
    stack.size+=1
    
def top(stack):           #peak
    if empty_stack(stack):
        raise IndexError("stack is empty")
    return stack.top.item
    
def pop(stack):
    item=top(stack)
    stack.top=stack.top.next
    stack.size-=1
    return item