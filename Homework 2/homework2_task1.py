"""
file: homework2_task1.py
language: python3
author: mjoscl@rit.edu Michael J. O'Connor
description: homework 2 task 1, assigned mon-8-29-16, due sat-9-3-16
"""

def divisible(x,y):
    """
    Tests to see if x or y are negative, and print the warning.
    Then tests to see if x & y are equal, and prints that warning.
    Then determines which of the numbers is greater.
    Then determines if the number is divisible evenly by the other
    and outputs the correct response
    """
    if ((x<0) or (y<0)):
        print("Inputs must be positive integers!")
    elif (x==y):
        print("Those numbers are equal!")
    else:
        if (x>y):
            if ((x%y)!=0):
                print(x,"is not divisible by",y)
            else:
                print(x,"is divisible by",y)
        else:
            if ((y%x)!=0):
                print(y,"is not divisible by",x)
            else:
                print(y,"is divisible by",x)

def test_divisible():
	"""
	Tests each of the 6 potential conditions of divisible function
	"""
    """Test: one number negative"""
    divisible(-4,1)
    divisible(34,-8)
    """Test: numbers equal"""
    divisible(8,8)
    """Test: number 1 is greater than number 2 and has remainder"""
    divisible(20,3)
    """Test: number 1 is greater than number 2 and has no remainder"""
    divisible(20,4)
    """Test: number 2 is greater than number 1 and has remainder"""
    divisible(3,29)
    """Test: number 2 is greater than number 1 and has no remainder"""
    divisible(6,30)


test_divisible()
