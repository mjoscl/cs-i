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
    



def is_match(str1,str2):
    if str1==str2:
        return True
    return False

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
        

def match_word(words_list):
    input_str=""
    while input_str != "<QUIT>":
        result_list = []
        input_str=input("Please enter a word to search for:")
        for word in words_list:
            if is_match(word,input_str):
                result_list+=[word]
        if len(result_list)>0:
            print("The word has been found")
        else:
            print("The prefix does not exist in the list")

if __name__ == "__main__":
    """ this is a description of what the main function does """
    words_file=input("Enter the name of the known words file:")
    #match_word(words_to_list(words_file))
    match_prefix(words_to_list(words_file))

"""
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

"""

# foo=True
# while fooo=True:
#  a=input("")
#  if a=="<QUIT">
#      foo=false
#  print(a)