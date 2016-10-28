"""
file: tour_utils.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: this is the utilities module that contains the utilities used
in lab6, the dippy, hippie tour. this file contains the class definition,
turtle methods, and 2 different traveling algorithms. this module can be
used in tour_list.py and tour_nearest.py.
"""


from rit_lib import *
import turtle
import math


class Places(struct):
    """
    this class describes a class with four slots that contain the locations'
    name, x-coordinate, y-coordinat, and a boolean flag called visited. the
    boolean slot is only relative in the tour_nearest algorithm, as the
    tour_list algorith doesn't need to track the locations that have been
    visited already.
    """
    _slots=((str,'name'),(float,'x'),(float,'y'),(bool,'visited'))
    
    
def turtle_init():
    """
    this function initializes the global settings for the turtle canvas. it
    creates the window which measures 600 by 600 pixels and creates
    a coordinate system of 1000x1000 inside that window, with a size-10 frame
    """
    turtle.setup(width=600, height=600)
    turtle.setworldcoordinates(-10, -10, 1010, 1010)
    turtle.up()
    turtle.setheading = 0
    turtle.goto(0, 0)
    

def travel_by_nearest(locations,current_location_index,target_location_index,trip_number):
    """
    this function moves the turtle to the designated location, then creates
    the necessary turtle output of a dot and label. then it calculates the
    distance traveled by calling calc_distance and returns that number as well
    as the string to output to the user about the order of the trips
    :param locations: the list of location objects
    :param type: list
    :param current_location_index:the index of the current object
    :param type: int
    :param target_location_index:the index of the target object
    :param type: int
    :param trip_number: the number trip of the algorithm
    :param type: int
    :return:trip_distance, trip_string
    :rtype:float, string
    """
    trip_string=""
    if trip_number==1:
        turtle.up()
        turtle.goto(locations[0].x,locations[0].y)
        turtle.down()
        turtle.dot(size=5)
        location_message = locations[0].name + " (" + str(format(locations[0].x, '.3f')) + "," + str(format(locations[0].y, '.3f')) + ")"
        turtle.write(location_message, align="right",font=("Arial", 10, "normal"))
        turtle.goto(locations[target_location_index].x,locations[target_location_index].y)
        turtle.dot(size=5)
        location_message = locations[target_location_index].name + " (" + str(format(locations[target_location_index].x, '.3f')) + "," + str(format(locations[target_location_index].y, '.3f')) + ")"
        turtle.write(location_message, align="right",
                     font=("Arial", 10, "normal"))
    elif trip_number > 1 and trip_number < len(locations):
        turtle.goto(locations[target_location_index].x,locations[target_location_index].y)
        turtle.dot(size=5)
        location_message = locations[target_location_index].name + " (" + str(format(locations[target_location_index].x, '.3f')) + "," + str(format(locations[target_location_index].y, '.3f')) + ")"
        turtle.write(location_message, align="right",font=("Arial", 10, "normal"))
    else:
        turtle.goto(locations[0].x,locations[0].y)
    locations[target_location_index].visited = True
    trip_string=" => "+locations[target_location_index].name
    trip_distance=calc_distance(locations[current_location_index].x,locations[current_location_index].y,locations[target_location_index].x,locations[target_location_index].y)
    return trip_distance,trip_string
    

def travel_by_list(places,current_location_index):
    """
    this function provides the functionality to tour_list.py by using the
    passed parameters of the list of objects and its current location on the
    list of objects, as indicated by the index. it then decides on which
    of the remaining locations will be the correct one to visit. once that
    decision is made. the turtle is moved to the next location. once there,
    the function drawes a dot and writes the location details. lastly, the
    function calculates the distance between the two points and returns it along
    with the string describing the move for later output
    :param places: the list of location objects with a name, x and y
    coordinates
    :param type: list
    :param current_location_index:
    :return:distance between the two points and information about the move
    :rtype: float and string
    """
    target_location_index=-1
    list_string=""
    if current_location_index == 0:
        target_location_index=1
    elif current_location_index > 0 and current_location_index < (len(places) - 1):
        target_location_index=current_location_index+1
    elif current_location_index == (len(places) - 1):
        target_location_index=0

    if current_location_index==0:
        turtle.up()
        turtle.goto(places[current_location_index].x,places[current_location_index].y)
        turtle.down()
        turtle.dot(size=5)
        location_message = places[current_location_index].name + " (" + str(format(places[current_location_index].x,'.3f')) + "," + str(format(places[current_location_index].y,'.3f')) + ")"
        turtle.write(location_message, align="right",font=("Arial", 10, "normal"))
        turtle.goto(places[target_location_index].x,places[target_location_index].y)
        list_string = places[current_location_index].name + " => " + places[target_location_index].name + " => "
    elif current_location_index > 0 and current_location_index < (len(places)-1):
        location_message = places[current_location_index].name + " (" + str(format(places[current_location_index].x, '.3f')) + "," + str(format(places[current_location_index].y, '.3f')) + ")"
        turtle.write(location_message, align="right",font=("Arial", 10, "normal"))
        turtle.goto(places[target_location_index].x,places[target_location_index].y)
        list_string = list_string + places[target_location_index].name + " => "
    elif current_location_index == (len(places)-1):
        turtle.goto(places[target_location_index].x,places[target_location_index].y)
        list_string = list_string + places[target_location_index].name
    turtle.dot(size=5)
    travel_distance=calc_distance(places[current_location_index].x,places[current_location_index].y,places[target_location_index].x,places[target_location_index].y)
    return travel_distance, list_string


def list_from_file(file):
    """
    this function reads each line of a file and returns a list of locations
    :param file: the name of the file to open
    :param type: str
    :return: list of locations with x and y coordinates
    :rtype:list
    """
    return_list=[]
    for i in open(file):
        return_list+=(i.strip()).split(",")
    return return_list


def file_to_objects():
    """
    this function prompts the user for a file that contains a list of the
    locations and their coordinates. this function iterates through each
    line and creates an object for each location. finally the function
    returns the entire list of objects
    :return: the list of place objects
    :rtype: list
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to the Dippy Hippie Tour. Get on the bus!")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    file_name=input("Enter filename:")
    list_of_places=list_from_file(file_name)
    places = []
    object_count = 0
    for e in range(0, len(list_of_places), 3):
        places += [Places(list_of_places[e].strip(), float(list_of_places[e + 1].strip()),float(list_of_places[e + 2].strip()),False)]
        object_count += 1
    print("Reading", file_name, "...", object_count, "places.")
    return places


def calc_distance(x1,y1,x2,y2):
    """
    :param x1: the x-coordinate of the original location
    :param type: float
    :param y1: the y-coordinate of the original location
    :param type: float
    :param x2: the x-coordinate of the target location
    :param type: float
    :param y2: the y-coordinate of the target location
    :param type: float
    :return: the total distance between the two points
    :rtype:float
    """
    total = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return total
    

if __name__ == "__main__":
    turtle_init()
    for i in file_to_objects():
        print(i)
    turtle.done()