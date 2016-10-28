"""
file: auto_complete.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:
use <> to sort
binary search [     ] > [      _|_       ]
"""


def words_to_list(file):
    lst=[]
    for line in open(file):
        lst += line.split()
    return lst


def is_prefix_match(word,prefix):
    #print("find",prefix,"-",word,"-",len(prefix),",",word[:len(prefix)])
    if prefix == word[:len(prefix)]:
        return True
    return False

def selection_sort(ss_list):
    """this is a description of what this function does
    :param int_list: a list of integers
    :type int_list: list
    :return: return the sorted list
    :rtype: list
    """
    for list_index in range(len(ss_list)):
        smallest_index = list_index
        for list_index2 in range(list_index + 1, len(ss_list)):
            if ss_list[list_index2] < ss_list[smallest_index]:
                smallest_index = list_index2
        swap(ss_list, smallest_index, list_index)
    return ss_list


def swap(ss_list, sorted_index, new_index):
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
    temp_int = ss_list[sorted_index]
    ss_list[sorted_index] = ss_list[new_index]
    ss_list[new_index] = temp_int


def binary_search(data, target, start, end):
    """
    binary_search : List(Orderable) Orderable NatNum NatNum -> NatNum or NoneType
    Perform a binary search for a target value between start and end indices.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
        start - the starting index in data that is part of this search
        end - the ending index in data that is part of this search
    Returns:
        index of target in data, if present; otherwise None.
    """
    #this code just searches for a match in the list provided
    #to change it
    
    #BELOW IS THE REGRESSION FORM - I WANT TO MAKE IT A WHILE LOOP
    
    match_found=False
    bs_list=[]
    while start <= end and match_found == False:
        mid_index = (start + end) // 2
        mid_value = data[mid_index]
        print("Searching for", target, ":", data[start:mid_index], "*" + str(mid_value) + "*", data[mid_index + 1:end + 1])
        if is_prefix_match(data[mid_index],target):
            bs_list+=data[mid_index]
            match_found=True
        elif target< data[mid_value]:
            end=mid_index-1
        else:
            start=mid_index+1
    
    """
    if start > end:
        return None
    mid_index = (start + end) // 2
    mid_value = data[mid_index]
    #print("Searching for", target, ":", data[start:mid_index],"*" + str(mid_value) + "*", data[mid_index + 1:end + 1])
    
    #if target == mid_value:
    if is_prefix_match(data, target):
        #add this index to the list
        return mid_index
    elif target < mid_value:
        return binary_search(data, target, start, mid_index - 1)
    else:
        return binary_search(data, target, mid_index + 1, end)
"""



def unsorted_search(prefix,words_list):
    result_list=[]
    for word in words_list:
        if is_prefix_match(word, prefix):
            result_list += [word]
    return result_list


def sorted_search(prefix,words_list):
    result_list=[]
    for word in selection_sort(words_list):
        if is_prefix_match(word, prefix):
            result_list += [word]
    return result_list



def eval_prefix(words_list):
    input_string=""
    last_prefix=""
    prefix_counter=0
    unsorted_list=[]
    sorted_list=[]
    bs_list=[]
    while input_string != "<QUIT>":
        input_string=input("Enter a prefix to search for:")
        if input_string==last_prefix:
            prefix_counter+=1
        else:
            last_prefix=input_string
            prefix_counter=0
        #FIND MATCH(es)
        #find match in unsorted linear search
        unsorted_list = unsorted_search(input_string, words_list)
        print("Prefix:",input_string,"& counter:",prefix_counter,"& len:",len(sorted_list))
        if len(unsorted_list) > 0 and prefix_counter >= len(unsorted_list):
            print("Unsorted List Element:(1)", unsorted_list[prefix_counter%len(unsorted_list)])
        elif len(unsorted_list) > 0 and prefix_counter < len(unsorted_list):
            print("Unsorted List Element:(2)", unsorted_list[prefix_counter])
        else:
            print("Unsorted List Element(3):",unsorted_list)
        #sort using selection or linear search and find prefix
        #sorted_list = sorted_search(input_string,words_list)
        #print("Sorted, matched list=", sorted_list)
        #sort using selection or linear, then find prefix using binary search
        #binary_search(data, target, 0, len(data) - 1)
        #bs_list = binary_search(selection_sort(words_list),input_string,0,(len(words_list)-1))
        #print("sorted, binary sought list=",bs_list)
        
        
        """
        -prompt for prefix
        once a prefix is entered:
        -prefix_counter=1
        -find a match in the linear unsorted method
        -if no match,return there are no matches
        -if match, make 3 lists
            -present first of lists
        -prompt for user input
        
        
        1-create a list of matches
        2-find matches
        3-create an unsorted linear search list and present first match
        4-create a sorted linear search list and present first match
        5-create a binary search list and present first match
        
        - need counter to keep track how many times the user uses same prefix
        """
        
        
        
        
        
        
        



def match_prefix(words_list):
    input_str=""
    while input_str != "<QUIT>":
        result_list = []
        input_str=input("Please enter a prefix to match for:")
        for word in words_list:
            if is_prefix_match(word,input_str):
                result_list+=[word]
        if len(result_list)>0:
            print("The prefix matches:",result_list)
                





if __name__ == "__main__":
    """ this is a description of what the main function does """
    words_file=input("Enter the name of the known words file:")
    #print("The unsorted list=",words_to_list(words_file))
    #print("The sorted list=",selection_sort(words_to_list(words_file)))
    eval_prefix(words_to_list(words_file))
    


""" def is_match(str1,str2):
    if str1==str2:
        return True
    return False

def search(prefix,a_list):
    searched_list=[]
    for word in a_list:
        if starts_with(prefix,word):
            searched_list+=[word]
    return searched_list

def linear_search(lst,search_for):
    pass

def binary_search(lst,search_for):
    pass



# foo=True
# while fooo=True:
#  a=input("")
#  if a=="<QUIT">
#      foo=false
#  print(a)
"""