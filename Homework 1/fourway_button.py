"""
file: fourway_button.py
language: python3
author: mjoscl@rit.edu Michael J. O'Connor
description: homework 1, assigned mon-8-22-16, due sat-8-27-16
"""


import turtle


def turtle_initialize():
    """
    resets the turtles properties to a known state:
    1-sets turtles location to origin
    2-faces the turtle north
    3-raises the pen
    """
    turtle.home()
    turtle.setheading(90)
    turtle.up()


def draw_border():
    """
    executes initialization to reset turtle
    Moves turtle forward away from the origin 150
    Sets the turtle's absolute heading to 180 and moves the turtle to the 
    starting point for drawing the border, which is at 180 degrees and 150 from
    the origin.
    Turtle begins to draw each leg of the square border each with a length of 
    300, only to end back at the starting point.
    The pen is then lifted.
    """
    turtle_initialize()
    turtle.forward(150)
    turtle.setheading(180)
    turtle.down()
    turtle.forward(150)
    turtle.setheading(270)
    turtle.forward(300)
    turtle.setheading(0)
    turtle.forward(300)
    turtle.setheading(90)
    turtle.forward(300)
    turtle.setheading(180)
    turtle.forward(150)
    turtle.up()  


"""
create a function that proceeds 100 forward and draws a triangle
all based from the initial heading passed by the parameter.
The triangle is drawn by drawing half of the bottom leg of the triangle which
is perpindicular from the line extending from the origin.
The turtle rotates 120 degrees and draws the second leg of the triangle.
The turtle rotates another 120 degrees and draws the third leg of the triangle.
Finally, the turtle rotates another 120 degrees to complete the half-drawn
first leg.
The pen is lifted.
"""
def draw_triangle(deg):
    turtle_initialize()
    turtle.setheading(deg)
    turtle.forward(100)
    turtle.right(90)
    turtle.down()
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(25)
    turtle.up()


"""
Creates a circle, centered around the origin with a diameter of 25.
First, initialize the turtle, faces 0 degrees then moves it 25 increments
from the origin.
Have the turtle face N, 90 degrees, otherwise the circle will no be centered.
Lower the pen.
Draw a circle with a diameter of 25.
Raise the pen.
"""
def draw_circle():
    turtle_initialize()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.setheading(90)
    turtle.down()
    turtle.circle(25)
    turtle.up()


""" Sets the appropriate title for this program """
turtle.title("Michael J. OConnor's Homework 1 Assigment for CS1")


""" call draw_border function to draw the outer border """
draw_border()


""" call draw_circle function to draw the circle in the center """
draw_circle()


""" call draw_triangle function with a parameter of 45 degrees so the 
function will draw a triangle in the 45 degree, or NE direction. """
draw_triangle(45)


""" call draw_triangle function with a parameter of 135 degrees so the 
function will draw a triangle in the 135 degree, or NW direction. """
draw_triangle(135)


""" call draw_triangle function with a parameter of 225 degrees so the 
function will draw a triangle in the 225 degree, or SW direction. """
draw_triangle(225)


""" call draw_triangle function with a parameter of 315 degrees so the 
function will draw a triangle in the 315 degree, or SE direction. """
draw_triangle(315)


""" call turtle_initialize to return the turtle to the starting position """
turtle_initialize()


""" move the turtle to the location where I will write my information """
turtle.goto(-90,90)


""" write to screen my information with some formatting to make it legible """
turtle.write("Michael J. O'Connor\nHomework 1\nCS1\n8-25-16", True, align="center",font=("Arial",12,"normal"))


""" include this so the screen does not close once the writing is complete """
turtle.done()