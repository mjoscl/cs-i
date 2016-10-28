from rit_lib import *
from stu import *
import random


class HashTable(struct):
    _slots=((int,'size'),(int,'capacity'),(object,'hash_func'),(list,'table'))
    

class Entry(struct):
    _slots=((object,'key'),(object,'value'))
    #this goes in table
    

def create_hash_table(capacity,hash_func):
    table=[None for _ in range(capacity)] #list comprehension, _indicates use this, without a name, bc if a name, will never use it
    #Create list with 1 None for every capacity
    #Create and pre-populate list
    #table = [i for i in range(capacity)] - other way
    return HashTable(0,capacity,hash_func,table)

def indexing_func(table,key):
    hashcode=table.hash_func(key) #key can be any type of object
    return hashcode%table.capacity


def put(hashtable, key, value):
    index=indexing_func(hashtable,key)
    entry=Entry(key,value)
    if not hashtable.table[index] is None:
        #search from here to find a linear search
        print("COLLISION at ",index,"!")
        for i in range(index,hashtable.capacity):
            if hashtable.table[i] is None:
                #put here
                print("found empty spoace at",i)
                index=i
                break
            else:
                current=hashtable.table[i]
                if current.key==key:
                    print("found duplicate")
                    return
                
        
    hashtable.table[index]=entry

hashtable=create_hash_table(15,hash_student)

#for i in range(15):
#    student=Student(str(random.randint(1,999999999)),0)
#    put(hashtable,student.id,student)

student=Student('111111111',0)
student=Student('111111111',0)
put(hashtable,student.id,student)

print(hashtable.table)


    