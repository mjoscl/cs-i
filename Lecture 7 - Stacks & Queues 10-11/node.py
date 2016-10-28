from rit_lib import *
from stack import *

class Node(struct):
    _slots=((object,'item'),((NoneType,'Node'),'next'))
    #object slot just means any data type can go in - weakly typed
    #'next' can have a value of NoneType (if tail) or 'Node'
    #'Node' doesnt exist at time of delcaration, but will later
    #you cant' refer to the class in its own declaration, use string


node1=Node(123,None)
node2=Node("abc",node1)
node3=Node([1,2,3],node2)

node=node3

while not node is None:
    print(node)
    node=node.next
