"""
file: lru.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: homework 6

"""

from rit_lib import *

def put_in_cache(entry,cache):
    """
    this function installs the entry into the first 'empty' location in the cache
    and returns the index of the new entry in the cache.
    @precondition: The cache must not be full
    :param entry: the page (char) entry
    :type entry: the page to be loaded
    :param cache: the cache lists
    :type cache: fixed-size list
    :return: the index of the new entry in the cache
    :rtype: integer
    """
    #finds the first None cache location and creates the object with the entry there
    lowest_index=-1
    for location in range(len(cache)):
        if cache[location]==None:
            lowest_index=location
            break
            
    #create object
    cache[lowest_index]=LRUEntry(entry,lowest_index)
        
    #print("Put",entry," into the first None in:",cache)
    return lowest_index

def position_in_cache(request,cache):
    """
    checks to see if the the request is in the cache. If it is, it returns the index
    of the cache entry that matches it
    :param request: the request to search for
    :type request: string
    :param cache: the cache list
    :type cache: fixed-size list
    :return: returns the index
    :rtype: integer
    """
    return_value=0
    for memory_requests in range(len(cache)):
        if cache[memory_requests] == request:
            return_value=memory_requests
        else:
            return_value=len(cache)
            
    return return_value


def find_LRU(cache):
    """
    Finds and returns the entry of the LRU cache item ( the lowest indexed non-None number).
    Also finds and returns the entry in the cache. It does this by returning an instance of tuple data type. This
    finds a spot to put a miss when the cache is already full
    :param cache: the cache list
    :type cahce: fixed-size list
    :return: object
    :rtype: tuple
    """
    lru_index=0
    lru_time=cache[0].time
    #find the lowest chache[i].time
    for locations in range(len(cache)):
        #if the time of this value is less than lru_time, chacnge lrut_time
        #print("L",locations,"F",cache[locations].time)
        if cache[locations].time<lru_time:
            print("***",cache[locations].time,"<",lru_time)
            lru_time=cache[locations].time
            lru_index=locations
        
        
    return lru_index


def run_LRU(cache,request):
    """
    Implements the LRU algorithm on the memory request string. It takes a cache of enries and a memeory request
    string which represents the time sequence of page requests in a simulation. It loops through the request string
    from start to finish. Each request[index] represent the next memory page to access in sequence. The index
    value is the time of access.
    :param cache: the complete cache list
    :type cache: list
    :param request: the memory request string
    :type request:string
    :return: return description
    :rtype: the return type description
    """
    misses=0
    for access_time in range(len(request)):
        #determine if miss or hit (i.e., isthe request(access_time)in the cache)
        #check to see if in cache
        if position_in_cache(request[access_time],cache) != len(cache):
            print("Time:", access_time, " Request:", request[access_time],"HIT.")
        else:
            cache_full=True
            for location in range(len(cache)):
                if cache[location] == None:
                    cache_full=False
            if cache_full==True:
                #Cache is full. find victim (lowest time value) - replace with new entry
                #print("Cache is full, victim:",find_LRU(cache))
                
                print("Time:", access_time, " Request:", request[access_time], "MISS. Victim: ", find_LRU(cache) ," Cache:",cache)
            else:
                #Cache is not full. place request[access_time] in first_none
                #print("New location:",put_in_cache(request[access_time],cache))
                #index_to_put_into=put_in_cache(request[access_time],cache))
                print("Time:", access_time, " Request:", request[access_time], "MISS. Victim: _ Cache:",cache)
            
            misses+=1
        
    return misses






class LRUEntry(struct):
    _slots=((str,'page'),(int,'time'))
    #page is the character representing the memory location that is stored in the cache entry
    #time represents the ime when the page was last accessed





if __name__ == "__main__":
    #Prompt the user for input
    #Initialize and run the simulation
    #one letter represents as request to access a single memory location
    #string of letters represents a sequence of memory ocation accesses
    #fixed-size list of objects represetn the cache of memory pages
    cache_size=0
    while cache_size <= 1:
        cache_size=int(input("Enter size of cache:"))
    cache=[]

    for location in range(cache_size):
        cache+=[None]
    
    
    #print(cache)
    #memory_request_string=input("Enter the string of memory requests:")
    memory_request_string = "abcbcbadcbbadefdac"
    
    print("Least Recently Used (LRU) Algorithm")
    print("Cache Size:",len(cache))
    print("Memory Request String:",memory_request_string)
    
    print("Miss count:",run_LRU(cache,memory_request_string))
    