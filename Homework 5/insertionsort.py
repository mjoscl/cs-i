"""
file: insertionsort.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: This assignment (homework 5) accepts the user input of a file containing integers on
new lines. The functions take the input as a list. The list is then sorted and returned to the user.

"""


def get_list():
    """
    This function prompts the user for a file, assignes each int into a list, and returns the list
    :return: returns the list
    :rtype: list
    """
    source_file = input("What is the filename?")
    open_file = open(source_file)
    return_list = []
    for line in open_file:
        return_list += [int(line.strip())]
    return return_list

def insertion_sort(a_list):
    """
    :param a_list: the unsorted list that must be sorted
    :type a_list: list
    :return: the sorted list returned back to main
    :rtype: list
    """
    length = len(a_list)
    for last_sorted in range(length-1):
        insert(a_list,last_sorted)
    return a_list

def swap(a_list,i,j):
    tmp=a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = tmp
    
def insert(a_list,last_sorted):
    index=last_sorted
    while index >= 0 and a_list[index] > a_list[index+1]:
        swap(a_list,index,index+1)
        index-=1


def is_sorted(a_list):
    length=len(a_list)
    for i in range(1,length):
        if a_list[i-1] > a_list[i]:
            return False
    return True

if __name__ == "__main__":
    """
    This is the main function that will control the calls and flow of the program.
    This simple program creates a list by calling get_list, and ultimately pass that to
    the sort_list function where it is sorted and returned.
    """
    my_list = get_list()
    print("The unsorted list:", my_list)
    print("The insertion sorted list:", insertion_sort(my_list))

