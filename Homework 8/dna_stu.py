"""
Program with three basic DNA functions that are used in
conjunction with a test function for homework.

File: dna_stu.py
Author: Aaron Deever
Author: add your name here
"""

from slList_stu import *

def constructDnaList(dnaString):
    """
    Given a DNA string, converts it into a list in which
    each character is a node.
    :param dnaString: string of DNA
    :return: dna string as a list
    """

    # PUT YOUR IMPLEMENTATION HERE
    dnaList=createList()
    for nucleotide in dnaString:
        append(dnaList,nucleotide)
    return dnaList

def convertDnaListToString(lst):
    """
    Given a dna string in list form, convert back to string
    :param lst: dna list
    :return: dna as string
    """

    # PUT YOUR IMPLEMENTATION HERE
    dna_string = ""
    if lst.head != None:
        cursor=lst.head
        while cursor != None:
            dna_string=dna_string+str(cursor.data)
            cursor=cursor.next
    return dna_string
        
    
    

def isPairing(lst1, lst2):
    """
    tests if the two strings are dna complementary base pairs.
    A must match with T, G with C.  Strings must be same length too.
    :param lst1: first dna list
    :param lst2: second dna list
    :return: boolean True if match, False else
    """

    # PUT YOUR IMPLEMENTATION HERE
    bool_return=False
    if lst1.size==lst2.size and (lst1.size==0 and lst2.size==0):
        bool_return=True
    elif lst1.size==lst2.size and (lst1.size>0 and lst2.size>0):
        cursor1=lst1.head
        cursor2=lst2.head
        number_of_matches=1
        while cursor1.next != None:
            if is_nucleotide(cursor1.data) and is_nucleotide(cursor2.data):
                if is_match(cursor1.data, cursor2.data):
                    number_of_matches+=1
            cursor1=cursor1.next
            cursor2=cursor2.next
        if number_of_matches==(lst1.size):
            bool_return=True
    return bool_return



def is_nucleotide(data):
    if data=="A" or data=="C" or data=="G" or data=="T":
        return True
    
    
    
def is_match(base1,base2):
    if (base1=="G" and base2=="C") or (base1=="C" and base2=="G") or (base1=="A" and base2=="T") or (base1=="T" and base2=="A"):
        return True
    else:
        return False