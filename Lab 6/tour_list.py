"""
file: tour_list.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:this is one of the programs for lab6 called the dippy hippie tour.
this one follows a list method of determining the next best location to travel
to and proceeds sequentially.
"""
from rit_lib import *
import tour_utils
import turtle

if __name__ == "__main__":
    tour_utils.turtle_init()
    locations=[]
    locations=tour_utils.file_to_objects()
    trip_distance=0
    total_distance=0
    trip_string=""
    list_string=""
    for index in range(len(locations)):
        trip_distance,trip_string = tour_utils.travel_by_list(locations,index)
        total_distance+=trip_distance
        list_string+=trip_string
    print(list_string)
    print("Distance:",total_distance)
    print("Close the canvas window to quit.")
    turtle.done()