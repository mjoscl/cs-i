"""
file: selectionsort.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: This assignment (homework 5) accepts the user input of a file containing integers on
new lines. The functions take the input as a list. The list is then sorted and returned to the user.

questions:
1. In what kind of test case does insertion sort perform better than selectionsort? Clearly describe the test case.
    Insertion sort should be chosen over selection sort in lists where there are anticipated to be more
    comparisons done, and not many movements. Selection sort would be a better choice for those lists where more
    movements/swaps will be anticipated. Insertion sort handles the determination of which is the next element
    to be evaluated better than selection sort because the next element to be evaluated for insertion sort is the
    first element in the unsorted substring. The test case would be a list of elements that are nearly sorted, or where
    the swaps only have to be within an element or two. Efficiency is lost when a large number of long-distance
    swaps are necessary to sort the list.

2. Why does selection sort perform worse than insertion sort in that test case?
    Selection sort would be a more inefficient choice than insertion sort on a list of mostly-ordered, small-distance
    swaps because a large amount of iteration is needed to obtain the next element that needs to be sorted (insertion
    sort knows exactly where it is). So even if the list is partially ordered, selection sort finds the next
    element to be sorted by comparing every element in the unsorted sublist.
"""


def get_list():
    """
    This function prompts the user for a file, assignes each int into a list, and returns the list
    :return: returns the list
    :rtype: list
    
    the file I am using is called int_list.txt
    """
    source_file = input("What is the filename?")
    open_file = open(source_file)
    return_list = []
    for int_value in open_file:
        return_list += [int(int_value.strip())]
    return return_list


def sort_list(int_list):
    """this is a description of what this function does
    :param int_list: a list of integers
    :type int_list: list
    :return: return the sorted list
    :rtype: list
    """
    for list_index in range(len(int_list)):
        smallest_index = list_index
        for list_index2 in range(list_index + 1, len(int_list)):
            if int_list[list_index2] < int_list[smallest_index]:
                smallest_index = list_index2
        swap(int_list, smallest_index, list_index)
    return int_list


def swap(int_list, sorted_index, new_index):
    """
    This function accepts the list to replace the end of hte sorted list (sorted_index) with the
    next sorted value (new_index)
    :param int_list: a list of integers
    :type int_list: list
    :param sorted_index: this is the current index of hte last sorted  value
    :type sorted_index: int
    :param new_index: the index of hte element that ris the newest adfdition to the sorted list
    :type new_index: int
    """
    temp_int = int_list[sorted_index]
    int_list[sorted_index] = int_list[new_index]
    int_list[new_index] = temp_int


if __name__ == "__main__":
    """
    This is the main function that will control the calls and flow of the program.
    This simple program creates a list by calling get_list, and ultimately pass that to
    the sort_list function where it is sorted and returned.
    
    the file I am using is called int_list.txt
    """
    my_list = get_list()
    print("The unsorted list:", my_list)
    print("The sorted list:", sort_list(my_list))

