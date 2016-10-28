"""
file: shapy_turtle.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:

"""

import turtle

def turtle_turn_left(degrees):
    """
    this function turns the turtle left (counter-clockwise) to the extent
    determined by the parameter in degrees
    :param degrees: the number of degrees to rotate the turtle
    :type degrees: integer
    """
    print ("Turn left by:",degrees,"degrees")
    #turtle.left(int(degrees))


def turtle_turn_right(degrees):
    """
    this function turns the turtle right (clockwise) to the extent
    determined by the parameter in degrees
    :param degrees: the number of degrees to rotate the turtle
    :type degrees: integer
    """
    print("Turn right by:", degrees, "degrees")
    #turtle.right(int(degrees))


def turtle_draw_square(length):
    """
    this function draws a square, in the counter-clockwise direction, with
    lengths determined by the parameter
    :param length: the length of each side of the square to be drawn
    :type length: integer
    """
    turtle.forward(int(length))
    turtle.left(90)
    turtle.forward(int(length))
    turtle.left(90)
    turtle.forward(int(length))
    turtle.left(90)
    turtle.forward(int(length))


def turtle_draw_triangle(length):
    """
    this function draws a triangle, in the counter-clockwise direction, with
    side lengths determined by the parameter length
    :param length: the length of each side of the triangle to be drawn
    :type length: integer
    """
    turtle.forward(int(length))
    turtle.left(120)
    turtle.forward(int(length))
    turtle.left(120)
    turtle.forward(int(length))

def turtle_draw_circle(radius):
    """
    this function draws a circe, with radius -radius-, in the counter-clockwise
    direction, with
    side lengths determined by the parameter length
    :param radius: the radius of the circle to be drawn
    :type radius: integer
    """
    turtle.circle(int(radius))


def turtle_forward(distance):
    turtle.forward(int(distance))


def turtle_backward(distance):
    turtle.backward(int(distance))


def turtle_pen_up():
    turtle.up()


def turtle_pen_down():
    turtle.down()


def turtle_draw_rectangle(l, w):
    turtle.left(90)
    turtle.forward(int(l))
    turtle.left(90)
    turtle.forward(int(w))
    turtle.left(90)
    turtle.forward(int(l))
    turtle.left(90)
    turtle.forward(int(w))


def turtle_draw_polygon(sides, length):
    pass


def turtle_goto(x, y):
    turtle.setposition(int(x),int(y))


def turtle_color(color_name):
    turtle.pencolor(color_name)


def turtle_init():
    """
    this function initializes the window and p
    :param degrees: the number of degrees to rotate the turtle
    :type degrees: integer
    """
    turtle.clear()
    turtle.title("Michael J. O'Connor's CS1 Lab 4")
    turtle.setheading(0)
    turtle.setposition(0, 0)
    turtle.down()


def get_length(string):
    """
    this function takes the string and returns the recursively-calculated
    length
    :param string: the string to find the length of
    :type string: string
    :return: the integer number representing the length of the string
    :rtype: int
    """
    if string == "":
        return 0
    else:
        head = string[0]
        tail = string[1:]
    return 1 + get_length(tail)


def get_numbers(string):
    return_number = ""
    for char in string:
        if char.isdigit():
            return_number = return_number + char
        else:
            return return_number
    return return_number


def process_c(string):
    """
    this function parses the string to determine which commands and values to
    send to which functions.
    :param param1_name: description
    :type param1_name: type description
    """
    trim_at = 0
    counter = 0
    command=""
    string=string.strip()
    print("Original Command String:",string)
    for character in string:
        if character == "<":
            #turtle_turn_left(int(get_numbers(string[counter+1:])))
            print("turtle_turn_left")
            string = string[1+get_length(get_numbers(string[counter+1:])):]
        elif character == ">":
            #turtle_turn_right(get_numbers(string[counter + 1:]))
            string = string[1 + get_length(get_numbers(string[counter + 1:])):]
        elif character == "S":
            command = ("draw square,counter=",counter," and ")
            #turtle_draw_square(length)
        elif character == "T":
            command = ("draw triangle,counter=",counter," and ")
            #turtle_draw_triangle(length)
        elif character == "C":
            command = ("draw circle,counter=",counter," and ")
            #turtle_draw_circle(radius)
        elif character == "F":
            turtle_forward(int(get_numbers(string[counter+1:])))
            string = string[1 + get_length(get_numbers(string[counter + 1:])):]
        elif character == "B":
            command = ("go backweard,counter=",counter," and ")
            #turtle_backward(distance)
        elif character == "U":
            command = ("pen up,counter=",counter," and ")
           # turtle_pen_up()
        elif character == "D":
            command = ("pen down,counter=",counter," and ")
            #turtle_pen_down()
        elif character == "R":
            command = ("draw rectangle,counter=",counter," and ")
            #turtle_draw_rectangle(l,w)
        elif character == "P":
            command = ("draw polygon,counter=",counter," and ")
            #turtle_draw_polygon()
        elif character == "G":
            command = ("goto point,counter=",counter," and ")
            #turtle_goto()
        elif character == "Z":
            command = ("change color of turtle,counter=",counter," and ")
            #turtle_color(color_name)
        print("New string:",string)
        string = string[counter:]

        counter = counter + 1



def test_process_c():
    """ Tests each of the flow decisions for validity """
    process_c("<120F30<120F30<120F30>90S30")
    process_c("F4>45F4<45F4<45F4<45F4")
    process_c("F10<90F10>90F9<90F9>90F8<90F8>90F7<90F7>90F6")


if __name__ == "__main__":
    """ this is a description of what the main function does """
    turtle_init()
    #test_process_c()
    process_c("F4>45F4<45F4<45F4<45F4")
    #process_c("<120F30<120F30<120F30>90S30")
    #process_c("F10<90F10>90F9<90F9>90F8<90F8>90F7<90F7>90F6")

    turtle.done()