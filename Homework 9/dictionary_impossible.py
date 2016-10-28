"""
file: dictionary_impossible.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: homework 9
this program accepts two text files, one with plain text to be encoded and
decoded and the other has the key:value pairs to use in those processes. The
plain text is encoded, returned to the user, then decoded and returned back
to the user.
"""

from rit_lib import *
       

def encode(plain_text_file,key_file):
    """
    this function accepts the two files as parameters. it then creates a hash
    table for the encoding process and populates it from the key_file. then the
    function encodes the plain text file and returns the encoded list back to
    main
    :param plain_text_file: the filename of the file containing the plain text
    :param key_file: the filename of the file containing the key/value pair
    :return: the plain text as an encoded list
    """
    hash_table = {}
    for line in open(key_file):
        key, value = ((line.strip()).split(" "))
        hash_table[key] = value
    print(hash_table)
    
    encoded_list=[]
    for line in open(plain_text_file):
        return_line=""
        for word in line.split():
            return_line=return_line+hash_table[word] + " "
        encoded_list+=[return_line.strip()]
    
    print("Sending the encoded lines to the agent.")
    print("The encoded lines are:")
    return encoded_list


def decode(encoded_list,key_file):
    """
    this function accepts the encoded list and the key_file. it creates a hash
    table for the decoding process and populates it from the key_file. then
    the function decodes the encoded list and prints each line as they are
    decoded
    :param encoded_list: the list of the encoded pain text
    :param key_file: the filename of the file containing the key/value pair
    :return: None
    """
    decode_table = {}
    for line in open(key_file):
        key, value = ((line.strip()).split(" "))
        decode_table[value] = key
    print("The <encode_word,word> pairs are:")
    print(decode_table)
    for line in encoded_list:
        return_line=""
        for word in line.split():
            return_line=return_line+decode_table[word]+" "
        print(return_line.strip())


def main():
    """
    This main function runs the simulation and prompts for and calls the
    respctive functions, returning all messages to the user
    :return: None
    """
    print("Welcome to the Encoder 2000!")
    key_file="secret_key.txt"
    plain_text_file="plain_text.txt"
    print("Preparing to encode",plain_text_file,"using",key_file)
    print("The <word, encode_word> pairs are:")
    encoded_list=encode(plain_text_file,key_file)
    print(encoded_list)
    print("The agent is decoding the lines.")
    decode(encoded_list,key_file)
    print("Exiting the Encoder 2000!")


if __name__ == "__main__":
    """ the main function that executes upon run and calls the main function """
    main()