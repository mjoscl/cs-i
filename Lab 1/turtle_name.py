"""
file: turtle_name.py
language: python3
author: mjoscl@rit.edu Michael J. O'Connor
description: lab 1, assigned fri-8-26-16, due tue-8-30-16
write "TURTLE MJOSCL@RIT.EDU"
"""

import turtle


def initBannerCanvas():
    """
    Sets up the canvas and the world so that it is 1200 wide and 80 tall.
    Also sets the origin to be 5 pixels from the left and from the bottom.
    Sets the default pen properties to up, size of 2 and speed of 5.
    """
    turtle.setup(1200,80)
    turtle.setworldcoordinates(-5,-5,455,35)
    turtle.up()
    turtle.pensize(2)
    turtle.speed(5)


def draw_R():
    """
    Writes the letter R and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(12.5)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(153.4)
    turtle.forward(28)
    turtle.up()
    turtle.left(26.6) #ALWAYS FACEE EAST 2 cirlces and a line
    turtle.forward(5)
    
    
def draw_I():
    """
    Writes the letter I and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(25)
    turtle.down()
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(180)
    turtle.forward(12.5)
    turtle.right(90)
    turtle.down()
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(20)
    
    
def draw_T():
    """
    Writes the letter T and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.left(90)
    turtle.forward(25)
    turtle.down()
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(180)
    turtle.forward(12.5)
    turtle.down()
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(15)

def draw_L():
    """
    Writes the letter L and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.left(90)
    turtle.forward(25)
    turtle.down()
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.forward(5)


def draw_U():
    """
    Writes the letter U and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.left(90)
    turtle.forward(25)
    turtle.down()
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)
    
def draw_spacer():
    """
    This moves the turtle forward 10 spaces to act as a spacer.
    """
    turtle.forward(10)

def draw_dot():
    """
    Writes the dot and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(3)
    turtle.left(90)
    turtle.up()
    turtle.forward(8)
    
def draw_E():
    """
    Writes the letter E and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.right(90)
    turtle.forward(12.5)
    turtle.right(90)
    turtle.down()
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(12.5)
    turtle.left(90)
    turtle.down()
    turtle.forward(25)
    turtle.up()
    turtle.forward(5)


def draw_O():
    """
    Writes the letter O and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(30)

def draw_M():
    """
    Writes the letter M and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(53.1)
    turtle.forward(12.5)
    turtle.left(106.2)
    turtle.forward(12.5)
    turtle.right(53.1)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(5)

def draw_J():
    """
    Writes the letter J and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.left(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.down()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)

def draw_C():
    """
    Writes the letter C and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.forward(25)
    turtle.left(180)
    turtle.down()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)

def draw_S():
    """
    Writes the letter S and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(12.5)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(12.5)
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)

def draw_D():
    """
    Writes the letter D and returns the turtle to the default position
    of facing East, pen up, and at the bottom left corner of the next letter.
    """
    turtle.down()
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(7.05)
    turtle.left(45)
    turtle.forward(15)
    turtle.left(45)
    turtle.forward(7.05)
    turtle.left(45)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.left(90)
    turtle.forward(30)

def test_draw_R():
    initBannerCanvas()
    draw_R()
    turtle.done()

#test_draw_R()


initBannerCanvas()
draw_T()
draw_U()
draw_R()
draw_T()
draw_L()
draw_E()
draw_spacer() #SPACE
draw_M()
draw_J() 
draw_O()
draw_S()
draw_C()
draw_L()
draw_spacer()
turtle.write("@",align="center",font=("Arial",40,"normal"))
draw_spacer()
draw_R()
draw_I()
draw_T()    
draw_dot()
draw_E()
draw_D()
draw_U() 
turtle.done()