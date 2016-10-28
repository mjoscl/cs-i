"""
file: homework2_task2.py
language: python3
author: mjoscl@rit.edu Michael J. O'Connor
description: homework 2 task 2, assigned mon-8-29-16, due sat-9-3-16
"""

def triangle(a,b,c):
    """
    Tests if a, b, or c are negative, then prints the message
    Tests the three combinations of a, b, and c to see if the sum of the 
    first two is greater than the last.
    If all three conditions are true, prints the message that a,b,c can form
    a triangle.
    If any of the conditions are false, prints the message that a,b,c can
    not form a triangle.
    """
    if ((a<0) or (b<0) or (c<0)):
        print("Triangles require sides of positive length!")
    else:
        if check_sides(a,b,c) and check_sides(b,c,a) and check_sides(c,a,b):
        #if (((check_sides(a,b,c)==True) and (check_sides(b,c,a)==True) and (check_sides(c,a,b)==True):
            print(a,b,"and",c,"can form a triangle.")
        else:
            print(a,b,"and",c,"can NOT form a triangle.")
            
            
            
def check_sides(x,y,z):
    """
    This returns true if the sum of x+y > z.
    This returns false otherwise    
    """
    if ((x+y)>z):
        return True
    else:
        return False         
                
def test_triangle():
    """
    Tests each of the decision-points for the triangle(a,b,c) function
    """
    """tests if a is negative """
    triangle(-3,6,5)
    """ tests if b is negative """
    triangle(6,-3,5)
    """ tests if c is negative """
    triangle(6,5,-3)
    """ tests if the triangle can be formed """
    triangle(5,8,12)
    """ tests if the triangle cannot be formed with these values """
    triangle(3,4,9)
    
test_triangle()