"""
file: ____.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:
"""

def binary_search(search_for,search_list):
    list_start = 0
    list_end = len(search_list)-1
    sorted=False
    while list_start <= list_end and not sorted:
        print("start=",list_start,"& end=",list_end,"& Midpoint=",(list_start+list_end)//2, "& list length=", len(search_list))
        print("List=",search_list[list_start:list_end])
        list_midpoint = (list_start+list_end)//2
        if search_for == search_list[list_midpoint]:
            sorted = True
        else:
            if search_for < search_list[list_midpoint]:
                list_end = list_midpoint-1
            else:
                list_start = list_midpoint+1
    return sorted


if __name__ == "__main__":
    """ this is a description of what the main function does """
    my_list=[1,14,20,56,90,234,2345]
    #print(my_list)
    print(binary_search(14,my_list))
    