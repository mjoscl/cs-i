"""
file: bowties.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: this program recurcively draws bowties following a specific
algorithm while using lengths of 100 and a recurcive depth of 0-3, as 
specified by the user
"""

import turtle


def get_depth():
    """
    this function asks the user for the depth of the recursion, then converts
    it to an integer and returns it to main
    prerequisites: none
    postrequisites:none
    """
    return int(input("Please choose the depth of the recursion (0, 1, 2, 3):"))


def draw_bowties(length,depth):
    """
    this function ensures the depth value is greater than zero and then draws 
    the initial center bowtie with the referenced length. next, it moves to the
    position for the right bowtie and recurcively draws however many there.
    next, it returns to the center of the original bowties and draws the left
    side bowties. the two 180 degree turns are needed so that the right side
    bowtie does not draw samller (if depth > 2) on the relative bottom. lastly,
    turtle returns to the original starting position
    precondition:turtle is facing right and pen up
    postcondition:turtle is facing right and pen up
    """
    if depth==0:
        pass
    else:
        draw_bowtie(length)
        #orient to draw top right bowtie(s)
        turtle.left(30)
        turtle.forward(2*length)
        draw_bowties(length/3,depth-1)
        #orient to draw top left bowtie(s)
        turtle.backward(2*length)
        turtle.left(120) 
        turtle.forward(2*length)
        turtle.right(180)
        draw_bowties(length/3,depth-1)
        turtle.left(180)
        #orient back home
        turtle.backward(2*length)
        turtle.right(150)

def draw_circle(radius):
    """
    this function draws a circle of in the middle of the bowtie with a 
    radius of 0.25 the passed referenced length
    precondition:turtle is facing right and pen up
    postcondition:turtle is facing right and pen up
    """
    turtle.up()
    turtle.right(90)
    turtle.forward(0.25*radius)
    turtle.left(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(0.25*radius)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(0.25*radius)
    turtle.right(90)

    
def draw_bowtie(length):
    """
    this function draws a bowtie with sides length and a circle in the middle
    precondition:turtle is facing right and pen up
    postcondition:turtle is facing right and pen up
    """
    turtle.down()
    turtle.left(30)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(2*length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.right(30)   
    draw_circle(length) 


def test_draw_bowties():
    """
    this function tests all the possible inputs for the draw_bowties() function
    """
    #draw_bowties(100,0)
    #draw_bowties(100,1)
    #draw_bowties(100,2)
    #draw_bowties(100,3)
    #draw_bowties(100,4)


if __name__=="__main__":
    """
    this main function sets up the canvas and window, including the colors of
    the pen and fill
    """
    
    """ this sets up the window's height and width to be 50% of the screen size"""
    turtle.setup(width=0.5, height=0.5)

    """ this sets up the title of the window to the string shown """    
    turtle.title("CSI-Lab2-Michael J. O'Connor")
    
    """ this sets the turtle's pen color to blue and the fill color to red """
    turtle.color("blue","red")
    
    """ this is the test function to test the functionality of draw_bowties """
    #test_draw_bowties()
    
    """ this is the primary call method to start drawing bowties with length
    100 and to prompt the user for the depth """
    draw_bowties(100,get_depth())    
    
    """ this statement keeps the window open once the turtle is done drawing """
    turtle.done()