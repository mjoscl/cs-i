from rit_lib import *
import math

class HashTable(struct):
    _slots = ((list, 'table'), (int, 'size'),
	          (int, 'capacity'), (object, 'hash_func'))



def create_hash_table(capacity,hash_func):
    table=[None for _ in range(capacity)]
    return HashTable(table,0,capacity,hash_func)

def hash_func(word):
    sum=0
    for i in range(0,len(word)):
        sum+=(ord(word[i])-ord("a"))*math.pow(31,i)


if __name__ == "__main__":
    h_table=create_hash_table(20,hash_func)
    for i in range(h_table.capacity):
        if h_table[i]==None:
            print("None")
        else:
            print("jasd")