"""
file: shapy_turtle.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: lab4 requires us to create an interpreter for turtle functions. it
will accept user input in command shorthand, process it, parse the inputted
string and call the appropriate functions with the appropriate parameters
to accomplish what the user intended. The functions include turning the turtle,
drawing a square, triangle, circle, polygon, rectangle, moving the turtle and
controlling its pen, and finally, the color of the turtle.

"""

import turtle

def get_command_string():
    """
    this function will process the input from the user and if the input
    is acceptable, it will initialize the turtle and call process_c, passing
    in the string from the user
    """
    command_string = input("Please enter the command string:")
    if not command_string == "":
        process_c(command_string)
    elif (not command_string[0] == "<") or (not command_string[0] == ">") or (
            not command_string[0] == "S") or (not command_string[0] == "T")or (
            not command_string[0] == "C") or (not command_string[0] == "F") or (
            not command_string[0] == "B") or (not command_string[0] == "U") or (
            not command_string[0] == "D") or (not command_string[0] == "R") or (
            not command_string[0] == "P") or (not command_string[0] == "Z") or \
            (not command_string[0] == "G") or (not command_string == ""):
        print("Error: Incorrect commands entered.")
    else:
        print("Error: No input detected.")


def initialize_turtle():
    """
    this function establishes defaults for the turtle for this program
    """
    turtle.clear()
    turtle.setheading(0)
    turtle.down()
    turtle.title("Michael J. O'Connor's Lab 4 for CS1")
    turtle.setposition(0,0)
    turtle.speed(10)


def get_length(string):
    """
    this function takes the string and returns the recursively-calculated
    length
    :param string: the string to find the length of
    :type string: string
    :return: the integer number representing the length of the string
    :rtype: integer
    """
    if string == "":
        return 0
    else:
        head = string[0]
        tail = string[1:]
    return 1 + get_length(tail)


def get_numbers(string):
    """
    this function takes the string and returns the leading numbers recusively
    :param string: the string to find the numbers of
    :type string: string
    :return: the string of numeric characters
    :rtype: string
    """
    return_number = ""
    #print("Get num str=",string)
    for char in string:
        if char.isdigit() or char=="-":
            return_number = return_number + char
        else:
            return return_number
    return return_number


def turtle_turn_left(degrees):
    """
    this function rotates the turtle to the left (counter-clockwise) the
    amount of degrees passed in the degrees variable
    :param degrees: the degree value analagous to the distance of the turn
    :type integer:
    """
    turtle.left(degrees)


def turtle_turn_right(degrees):
    """
    this function rotates the turtle to the right (lockwise) the
    amount of degrees passed in the degrees variable
    :param degrees: the degree value analagous to the distance of the turn
    :type integer:
    """
    turtle.right(degrees)


def turtle_draw_square(length):
    """
    this function accepts a value for the lengths of the four sides of a
    square that is to be drawn by the turtle
    :param length: the lengths of the sides
    :type integer:
    """
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)


def turtle_draw_triangle(side_length):
    """
    this function accepts a value for the lengths of the three sides of a
    triangle that is to be drawn by the turtle
    :param side_length: the lengths of the sides
    :type integer:
    """
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)


def turtle_draw_circle(radius):
    """
    this function accepts a value for the radius of acircle that is to be drawn
    by the turtle
    :param radius: the length of the radius
    :type circle:
    """
    turtle.circle(radius)


def turtle_move_forward(distance):
    """
    this function moves the turtle forward, in the direction it is facing
    'distance' amount
    :param distance: this is the distance to travel
    :type integer:
    """
    turtle.forward(distance)


def turtle_move_backward(distance):
    """
    this function moves the turtle backward, in the opposite direction it is
    facing 'distance' amount
    :param distance: this is the distance to travel
    :type integer:
    """
    turtle.backward(distance)


def turtle_pen_up():
    """
    this function tells the pen to pick its pen up
    """
    turtle.up()


def turtle_pen_down():
    """
    this function tells the pen to put its pen down
    """
    turtle.down()


def turtle_draw_rectangle(length,width):
    """
    this function accepts a value for the lengths and the widths of the
    fours sides of a rectangle to be drawn by the turtle
    :param length: the lengths of the longer sides
    :type integer:
    :param width: the lengths of the shorter sides
    :type integer:
    """
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)


def turtle_draw_polygon(sides,length):
    """
    this function has the turtle draw a polygon with 'sides' number of sides
    and 'length' length of the sides. It also calculates the angles
    :param sides:
    :type integer:
    :param length:
    :type integer:
    """
    #360/sides = angles
    angle=360/sides
    side_count=1
    while side_count<=sides:
        turtle.forward(length)
        turtle.left(angle)
        side_count = side_count + 1


def turtle_goto(x,y):
    """
    this turtle acceps a x and y value to use as a coordinates so that
    the turtle can be moved to that location on the screen
    :param x: the x value of the new location
    :type: integer
    :param y: the y value of the new location
    :type: integer
    """
    turtle.setposition(x,y)


def turtle_color(color_name):
    """
    this function accepts the name of the color that the function sets the
    turtle to
    :param color_name:
    :type: string
    """
    turtle.color(color_name)


def process_c(string):
    """
    This function parses each command from the string [assed from the user to
    the input function.
    :param string: this is the input string describing the actions the user
    wants the turtle to accomplish
    :type: string
    """
    print("The original string is:",string)
    string = string.strip()
    acc=0
    for character in string:
        if character == "<":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will turn left", temp_num, "degrees.")
            turtle_turn_left(int(temp_num))
            # put turtle back at default"""
        elif character == ">":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will turn right", temp_num, "degrees.")
            turtle_turn_right(int(temp_num))
            # put turtle back at default"""
        elif character == "S":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will draw a square with side length of",temp_num,".")
            turtle_draw_square(int(temp_num))
            #put turtle back at default
        elif character == "T":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will draw a triangle with side lengths of",temp_num,".")
            turtle_draw_triangle(int(temp_num))
        elif character == "C":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will draw a circle with a radius of", temp_num,".")
            turtle_draw_circle(int(temp_num))
        elif character == "F":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will move forward a distance of",temp_num,".")
            turtle_move_forward(int(temp_num))
        elif character == "B":
            temp_num = get_numbers(string[acc + 1:])
            print("The turtle will move backward a distance of",temp_num,".")
            turtle_move_backward(int(temp_num))
        elif character == "U":
            print("The turtle will raise its pen")
            turtle_pen_up()
        elif character == "D":
            print("The turtle will lower its pen")
            turtle_pen_down()
        elif character == "R":
            length = get_numbers(string[acc + 1:])
            width = get_numbers(string[(acc + 1 + get_length(length) + 1):])
            print("turtle will draw a rectangle with length",length,
                  "and width",width)
            turtle_draw_rectangle(int(length),int(width))
        elif character == "P":
            sides = get_numbers(string[acc + 1:])
            length = get_numbers(string[(acc + 1 + get_length(sides) + 1):])
            print("turtle will draw a ",sides,"sided polygon with length",length)
            turtle_draw_polygon(int(sides),int(length))
        elif character == "G":
            temp_x = get_numbers(string[acc+1:])
            temp_y = get_numbers(string[(acc+1+get_length(temp_x)+1):])
            print("turtle will move to location x=",temp_x,"y=",temp_y)
            turtle_goto(int(temp_x),int(temp_y))
        elif character == "Z":
            color_number = get_numbers(string[acc+1:])
            if color_number == "0":
                color_name = "red"
            elif color_number == "1":
                color_name = "blue"
            elif color_number == "2":
                color_name = "green"
            elif color_number == "3":
                color_name = "yellow"
            elif color_number == "4":
                color_name = "brown"
            else:
                color_name = "black"
            print("turtle color will be changed to",color_name)
            turtle_color(color_name)
        acc = acc+1


def test_process_c():
    """
    this function tests a variety of values to ensure that error-checking and
    the parsing of the process_c function is working correctly
    """
    #process_c("C100")
    #process_c("Z1R105,5G100,100>90C100>90UF100<180DS50F10T301P7,50")
    #process_c("R30,10UG50,50DS100")
    #process_c("S60F60Z0S60F60Z1S60")


if __name__ == "__main__":
    initialize_turtle()
    #test_process_c()
    command_string = get_command_string()
    turtle.done()
