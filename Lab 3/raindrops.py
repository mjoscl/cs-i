"""
file: raindrops.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:lab3 - this program creates a number of user-defined raindrops 
filled with a random color and ripples out with a random number of ripples. It
ensures that the raindrops and ripples remain within the screen.
"""

import turtle
import math
import random

#*****************************************************************************
#the following defines all the constants

def MAX_RAINDROPS():
    """
    this is a constant function which returns the constant named MAX_RAINDROPS
    with a value of 100
    :return: the maximum number of raindrops allowed, 100
    :rtype: int
    """
    return 100

def MAX_RAINDROP_RADIUS():
    """
    this is a constant function which returns the constant named 
    MAX_RAINDROP_RADIUS with a value of 20
    :return: the maximum size of the raindrops' radii
    :rtype: int
    """
    return 20

def MAX_NUMBER_RIPPLES():
    """
    this is a constant function which returns the constant named
    MAX_NUMBER_RIPPLES with a value of 8
    :return: the maximum number of ripples allowed, 8
    :rtype: int
    """
    return 8
    
def MIN_NUMBER_RIPPLES():
    """
    this is a constant function which returns the constant named
    MIN_NUMBER_RIPPLES with a value of 3
    :return: the maximum number of raindrops allowed, 3
    :rtype: int
    """
    return 3
    
def WINDOW_WIDTH():
    """
    this is a constant function which returns the constant named
    WINDOW_WIDTH which returns the width of the turtle window
    :return: the width of the turtle window in pixels
    :rtype: int
    """
    return turtle.window_width()
    
def WINDOW_HEIGHT():
    """
    this is a constant function which returns the constant named
    WINDOW_HEIGHT which returns the height of the turtle window 
    :return: the height of the turtle window in pixels
    :rtype: int
    """
    return turtle.window_height()

    #************************************************************

def test_constants():
    """
    this function lists all the constants and their values
    """
    print("Maximum number of raindrops:",MAX_RAINDROPS())
    print("Maximum number of ripples:",MAX_NUMBER_RIPPLES())
    print("Minimum number of ripples:",MIN_NUMBER_RIPPLES())
    print("Window Width:",WINDOW_WIDTH())
    print("Window Height:",WINDOW_HEIGHT())


def initialize_turtle():
    """
    this function sets the canvas and the default states of the turtle
    """
    turtle.up()
    turtle.speed(10)
    turtle.hideturtle()
    turtle.setheading(90)
    turtle.title("Michael J. OConnor's Lab 3 (CS1)")
    turtle.bgcolor("#336699")


def get_raindrop_number():
    """
    prompts the user for the number of raindrops then
    if the raindrop value is within the inclusive range of 1 and MAX_RAINDROPS,
    the function will return the int value and finally initiallizes the turtle
    """
    good_number=False
    raindrop_number=0
    while good_number==False:
        raindrop_number=input("Number of Raindrops (1-100):")
        if int(raindrop_number) > 0 and int(raindrop_number) <= MAX_RAINDROPS():
            good_number=True
            initialize_turtle()
    return int(raindrop_number)

    
def get_random_int(lower_limit,upper_limit):
    """
    this function generates a random integer using random.randomint within
    the range passed to it. Then it returns an integer
    :param lower_limit: the lower limit of the range to choose the random int
    :type lower_limit: int
    :param upper_limit: the upper limit of the range to choose the random int
    :type upper_limit: int
    :return: returns the integer within the designated range
    :rtype: int
    """
    return random.randint(lower_limit,upper_limit)

def get_random_number():
    """
    this function returns a random float between 0 and 1
    :return: random.random()
    :rtype: float
    """
	return random.random()

def circle_fits_in_window(x,y,radius):
    """
    this function accepts the x and y coordinates and radius of a circle to be
    drawn and tests to make sure that it fits in the screen
    this is done by ensuring that 4 points (representing N-90,W,180,S-270,E-0
    degrees is not more than the window end values
    if the circle will fit (i.e., none of the 4 points are outside the window,
    the function returns true, otherwise false
    :param x: the location of the circle's origin on the x axis
    :type x:float
    :param y:the loaction of the circle's origin on the y axis
    :type y: float
    :param radius: the radius of the desired circle
    :type radius: int
    :return: True if the circle fits, False otherwise
    :rtype: bool
    """
    if ((x+radius) < (WINDOW_WIDTH()/2)) and ((x-radius) > (-WINDOW_WIDTH()/2)) and ((y+radius) < (WINDOW_HEIGHT()/2)) and ((y-radius) > (-WINDOW_HEIGHT()/2)):
    	return True
    else:
        return False


def draw_raindrops(quantity):
    """
    this function ultimately draws [quantity] number of raindrops
    if quantity is greater than 1, random values are chosen for the turtle's
    location to draw the circle.
    After the circle's origin has been established, the drop is tested to 
    ensure at least the smallest of the ripples fits and then if so, the
    raindrop will be drawn and filled with a random color.
    Once the raindrop is done, the function calls the draw_ripples function to
    draw ripples around the raindrop.
    The function will recursively call itself to draw all the raindrops
    and computes and adds the area of all the drops as it unrolls the
    recursion.
    The last thing is to return the total surface area
    :param quantity: the number of raindrops to draw
    :type quantity: int
    :return: the area of all the raindrops added together
    :rtype: float
    """
    if quantity<1:
        return_value=0
    else:
        total_raindrop_area=0
        raindrop_fits=False
        while raindrop_fits==False:
            
            #get a x value that fits on the screen
            raindrop_x_fits = False
            while raindrop_x_fits==False:
                raindrop_x = get_random_number() * WINDOW_WIDTH()
                if raindrop_x < WINDOW_WIDTH():
                    raindrop_x_fits=True
                    window_x_zero=WINDOW_WIDTH()/2
                    if raindrop_x>window_x_zero:
                        raindrop_x = raindrop_x - (WINDOW_WIDTH()/2)
                    elif raindrop_x==window_x_zero:
                        raindrop_x = 0
                    elif raindrop_x<window_x_zero:
                        raindrop_x = -((WINDOW_WIDTH()/2)-raindrop_x)
                    
            #get a y value that fits
            raindrop_y_fits = False
            while raindrop_y_fits==False:
                raindrop_y = get_random_number() * WINDOW_HEIGHT()
                if raindrop_y < WINDOW_HEIGHT():
                    raindrop_y_fits=True
                    if raindrop_y>(WINDOW_HEIGHT()/2):
                        raindrop_y = raindrop_y - (WINDOW_HEIGHT()/2)
                    elif raindrop_y==(WINDOW_HEIGHT()/2):
                        raindrop_y = 0
                    elif raindrop_y<(WINDOW_HEIGHT()/2):
                        raindrop_y = -((WINDOW_HEIGHT()/2)-raindrop_y)
            
            
            raindrop_radius = get_random_int(1,MAX_RAINDROP_RADIUS()) 
            if circle_fits_in_window((raindrop_x-raindrop_radius),raindrop_y,raindrop_radius) and circle_fits_in_window((raindrop_x+(MIN_NUMBER_RIPPLES()*raindrop_radius)-raindrop_radius),raindrop_y,(MIN_NUMBER_RIPPLES()*raindrop_radius)):

                raindrop_fits=True
                turtle.setpos((raindrop_x+raindrop_radius),raindrop_y)
                turtle.down()
                turtle.fillcolor(get_random_number(),get_random_number(),get_random_number())
                turtle.begin_fill()
                turtle.circle(raindrop_radius)
                turtle.end_fill()
                turtle.up()
                draw_ripples(raindrop_x-raindrop_radius,raindrop_y,raindrop_radius)
                return_value=(math.pi*(math.pow(raindrop_radius,2))) + draw_raindrops(quantity-1)
    return return_value
    
def draw_ripples(x,y,radius):
    """
    :param x: the location of the circle's origin on the x axis
    :type x: float
    :param y: the location of the circle's origin on the y acis
    :type y: float
    :param radius: the distance from the origin of the circle to its edge
    :type radius: int
    :return: None
    """
    max_ripples_allowed=MAX_NUMBER_RIPPLES()
    found_ripple_number=False
    
    while found_ripple_number==False:
        if circle_fits_in_window(x+(radius*max_ripples_allowed-radius),y,(radius*max_ripples_allowed)):
            found_ripple_number=True
        else:
            if max_ripples_allowed<=3:
                found_ripple_number=True
            else:
                 max_ripples_allowed =  max_ripples_allowed - 1
    
    number_ripples_to_draw = get_random_int(MIN_NUMBER_RIPPLES(),max_ripples_allowed)
    
    number_ripples_left = 1
    while number_ripples_left<=number_ripples_to_draw:
        if circle_fits_in_window((x+(radius*number_ripples_left)),y,(radius * number_ripples_left+radius)):
            turtle.setheading(0)
            turtle.forward(radius*number_ripples_left)
            turtle.setheading(90)
            turtle.down()
            turtle.circle(radius * number_ripples_left+radius)
            turtle.up()
            turtle.setheading(180)
            turtle.forward(radius*number_ripples_left)
            turtle.setheading(90)
        number_ripples_left = number_ripples_left + 1
    
  
def test_main():
    test_constants()
         

if __name__ == "__main__":
    """
    this is the main function that will control the succession of calling the
    above functions.
    """
    #test_main()
    number_raindrops=get_raindrop_number()
    print("Total Area of ALL the Raindrops =",draw_raindrops(number_raindrops), " units")
    turtle.done()