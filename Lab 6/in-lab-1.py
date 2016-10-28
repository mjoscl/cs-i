from rit_lib import *

class Places(struct):
    _slot=((str,'name'),(float,'x'),(float,'y'))
    
    
def list_from_file(file):
    return_list=[]
    for i in open(file):
        #print(i.strip())
        return_list+=(i.strip()).split(",")
    return return_list

#split,strip


if __name__ == "__main__":
     list_of_places=list_from_file(input("Enter File Name:"))
     print("List=",list_of_places)