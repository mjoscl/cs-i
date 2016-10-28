"""
file: tour_nearest.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:this is one of the programs for lab6 called the dippy hippie tour.
this one determines which is the closest location that has not yet
 been visited to be the next best location to travel.
"""


from rit_lib import *
import tour_utils
import turtle


def find_closest_location_index(locations, current_location_index):
    """
    this function uses the relative distance in its algorithm to determine
    the next best place to visit.
    :param locations:this is the list of location objects
    :param type: list
    :param current_location_index:
    :param type: int
    :return: the index of the next closest location that has not yet been visited
    :rtype: int
    """
    closest_location_index = -1
    shortest_distance=-1
    for acc in range(len(locations)):
        if (acc != current_location_index) and (locations[acc].visited==False):
            temp_distance=tour_utils.calc_distance(locations[current_location_index].x,locations[current_location_index].y,locations[acc].x,locations[acc].y)
            if temp_distance < shortest_distance or shortest_distance==-1:
                shortest_distance=temp_distance
                closest_location_index=acc
    return closest_location_index


if __name__ == "__main__":
    tour_utils.turtle_init()
    locations = []
    locations = tour_utils.file_to_objects()
    trip_distance = 0
    total_distance = 0
    trip_string = ""
    list_string = ""
    number_of_trips=0
    current_location_index=0
    target_location_index=-1
    while number_of_trips < len(locations):
        if number_of_trips==0:
            current_location_index=0
            target_location_index=find_closest_location_index(locations,0)
            locations[0].visited=True
            list_string=locations[0].name
        elif number_of_trips>0 and number_of_trips<(len(locations)-1):
            target_location_index=find_closest_location_index(locations,current_location_index)
        else:
            target_location_index=0
        number_of_trips += 1
        trip_distance, trip_string = tour_utils.travel_by_nearest(locations,current_location_index,target_location_index,number_of_trips)
        current_location_index=target_location_index
        total_distance+=trip_distance
        list_string+=trip_string
        
    print(list_string)
    print("Distance:", total_distance)
    print("Close the canvas window to quit.")
    turtle.done()