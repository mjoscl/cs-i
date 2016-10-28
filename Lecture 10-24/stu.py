from rit_lib import *
import math

class Student(struct):
    _slots = ((str, 'id'), (int, 'credits'))


def hash_student(id):
    length=len(id)
    hashcode=0
    for i in range(length):
        c=id[i]
        ascii=ord(c)
        hashcode+=(ascii*math.pow(31,length-i-1))
    return int(hashcode)
#WHY DOES IT GO HERE?