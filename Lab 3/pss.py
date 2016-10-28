import turtle
import math

def draw_rec(radius,depth):
    if depth <= 0:
        return 0
    else:
        turtle.circle(radius*10)
        return (math.pi*(radius*radius)) + draw_rec(radius+1,depth-1)


print(draw_rec(4,4))
turtle.done