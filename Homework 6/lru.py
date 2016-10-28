"""
file: lru.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description: homework 6 is a simulation of a variation of Les Belady's algorithm to find
the most optimal page to remove from cache in order to add a requested page. it prompts
the user for the page sequence and number of cache memory locations. each request is
compared to any in memory. if a match exists, the time slot is updated, otherwise, a
victim must be found.the victim is the least recently used (i.e., oldest) page in the
cache. the lru class will be replaced or the empty location (indicated by None) will
be populated with an object of class LRUEntry. a counter tracks the number of misses
(when the request is not already loaded into cache).
"""


from rit_lib import *


def put_in_cache(entry,cache):
    """
    this function installs the entry into the first 'empty' location in the cache
    and returns the index of that new entry in the cache.
    @precondition: The cache must not be full
    :param entry: the page (char) entry
    :type entry: string
    :param cache: the fixed-sized list of cache locations
    :type cache: list
    :return: the index of the new entry in the cache
    :rtype: integer
    """
    lowest_index=-1
    for locations in range(len(cache)):
        if cache[locations]==None:
            lowest_index=locations
            break
    return lowest_index


def position_in_cache(request,cache):
    """
    checks to see if the the requested page is already in the cache.
    If it is, it returns the index of that cache location
    :param request: the page request to search for
    :type request: string
    :param cache: the fixed-sized list of cache locations
    :type cache: list
    :return: the index of the existing page, otherwise the cache size
    :rtype: integer
    """
    return_value=len(cache)
    for locations in range(len(cache)):
        if cache[locations] != None:
            if cache[locations].page==request:
                return_value=locations
    return return_value


def find_LRU(cache):
    """
    finds and returns the entry of the LRU cache location ( the lowest indexed non-None number) and
    returns the object index in the cache. This finds a spot to put a miss when the
    cache is already full
    :param cache: the fixed-sized list of cache locations
    :type cahce: list
    :return: index of the LRU cache location
    :rtype: tuple
    """
    
    lru_index=0
    lru_time=cache[0].time
    for locations in range(len(cache)):
        if cache[locations].time<lru_time:
            lru_time=cache[locations].time
            lru_index=locations
    return lru_index


def run_LRU(cache,request):
    """
    implements the LRU algorithm on the memory request string. It takes a list of memory cache locations
    and a memory request string which represents multiple individual page requests. It loops through
    the request string from start to finish. Each request[index] represent the next memory page
    to access in sequence. The index value is the time of access.
    :param cache: the fixed-sized list of cache locations
    :type cache: list
    :param request: the memory request string
    :type request:string
    :return: the total number of misses that occur
    :rtype: int
    """
    misses=0
    for access_time in range(len(request)):
        cache_full = True
        for locations in range(len(cache)):
            if cache[locations] == None:
                cache_full = False
        match_index=position_in_cache(request[access_time],cache)
        if match_index != len(cache):
            cache[match_index].time=access_time
            print("Time:", access_time, " Request:", request[access_time],"HIT.")
        else:
            if cache_full==True:
                victim_index = find_LRU(cache)
                victim_page=cache[victim_index].page
                victim_time=cache[victim_index].time
                cache[victim_index].page=request[access_time]
                cache[victim_index].time=access_time
                print("Time:",access_time,"Request:",request[access_time],"MISS. Victim: LRUEntry( page:", victim_page,"time:",victim_time,") Cache:", cache)
            else:
                new_object_index=put_in_cache(request[access_time],cache)
                cache[new_object_index] = LRUEntry(request[access_time], access_time)
                print("Time:", access_time, " Request:", request[access_time], "MISS. Victim: _ Cache:",cache)
            misses+=1
    return misses


class LRUEntry(struct):
    """
    this class creates an object with a page parameter (str) and a time parameter (int).
    these represent a request that is being held in the cache memory. the index of cache[index]
    will indicate the location, page will be a one-letter request and the time indicates which
    iteration the simulation is on.
    once created, the object can be called using cache[cache_location].page and
    cache[cache_location].time
    
    """
    _slots=((str,'page'),(int,'time'))
    #page is the character representing the memory location that is stored in the cache entry
    #time represents the ime when the page was last accessed


if __name__ == "__main__":
    """
    this main function controls the program by first prompting the user for both
    the request string and the size of the cache. then it creates a list the same size of
    the cache. lastly it calls run_LRU to begin the simulation, returning the number of
    missses that are then reported to the user.
    """
    cache_size=0
    while cache_size <= 1:
        cache_size=int(input("Enter size of cache:"))
    cache=[]
    for location in range(cache_size):
        cache+=[None]
    memory_request_string=input("Enter the string of memory requests:")
    print("Least Recently Used (LRU) Algorithm")
    print("Cache Size:",len(cache))
    print("Memory Request String:",memory_request_string)
    print("Miss count:",run_LRU(cache,memory_request_string))