import turtle
import math


def draw_rec(radius,depth):
    """ this function sets the canvas and the default states of the turtle """
    if depth <= 0:
        return 0
    else:
        turtle.circle(radius*10)
        return (math.pi*(radius*radius))+draw_rec(radius+1,depth-1)

def draw_iter(acc,radius):
    circum = 0
    while acc > 0:
        turtle.circle(radius)
        turtle.right(90)
        turtle.up()
        turtle.forward(radius)
        turtle.left(90)
        turtle.down()
        circum = circum + (math.pi*(2*radius))
        acc = acc - 1
        radius = radius + 1
    return circum

#draw_rec(3,3)
print("Area=",draw_iter(5,5))
turtle.done