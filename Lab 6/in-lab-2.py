from rit_lib import *
import turtle


class Places(struct):
    _slots=((str,'name'),(float,'x'),(float,'y'))
    
def turtle_init():
    turtle.up()
    turtle.setheading=0
    turtle.goto(0,0)
    turtle.setworldcoordinates(-10, -10, 1010, 1010)
    turtle.setup(width=600,height=600)
    
    
    
def list_from_file(file):
    return_list=[]
    for i in open(file):
        #print(i.strip())
        return_list+=(i.strip()).split(",")
    return return_list


if __name__ == "__main__":
     #turtle_init()
     file_name="p10.txt"
     #list_of_places=list_from_file(input("Enter File Name:"))
     list_of_places=list_from_file(file_name)
     
     places=[]
     
     object_count=0
     for e in range(0,len(list_of_places),3):
         places+=[Places(list_of_places[e].strip(),float(list_of_places[e + 1].strip()),float(list_of_places[e + 2].strip()))]
         object_count+=1
     print("Reading", file_name, "...", object_count, "places.")
     for i in range(len(places)):
         print(i,"- Location:",places[i].name,"at location: ",format(places[i].x,'.3f'),",",format(places[i].y,'.3f'))
         
     #turtle.done