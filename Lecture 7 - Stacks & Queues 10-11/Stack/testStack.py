"""
Test stack data structure.
file: testStack.py
author: Sean Strout
"""

from myStack import *

def main():
    # begin with an empty stack
    stackCh = createStack()
    print("Creating empty stack...")
    print("Stack empty?", True == emptyStack(stackCh))
    print("Stack size is 0?",  0 == stackCh.size)   
    
    # add first element
    print("push A...")
    push(stackCh, 'A')
    print("Stack not empty?", False == emptyStack(stackCh))
    print("Stack size is 1?", 1 == stackCh.size)   
    print("top is A?", 'A' == top(stackCh))
    
    # add second element
    print("push B...")
    push(stackCh, 'B')
    print("top is B?", 'B' == top(stackCh))
    
    # add third element
    print("push C...")
    push(stackCh, 'C')
    print("top is C?", 'C' == top(stackCh))
    print("Stack size is 3?", 3 == stackCh.size)   
      
    # pop top element, C
    print("pop...")
    pop(stackCh)
    print("Stack not empty?", False == emptyStack(stackCh))
    print("Stack size is 3?", 2 == stackCh.size)   
    print("top is B?", 'B' == top(stackCh))
    
    # add fourth element
    print("push D...")
    push(stackCh, 'D')
    print("top is D?", 'D' == top(stackCh))
    
    # Empty the stack
    print("Emptying the stack...")
    while not emptyStack(stackCh):
        print("Top of stack:", top(stackCh))
        print("pop...")
        pop(stackCh)
    
main()
