from stu import *
from class_hash_table import *


def get_student(students,id):
    for student in students:
        if student.id==id:
            return student
    return None


def get_credits(students,id):
    student=get_student(students,id)
    if not student is None:
        return student.credits
    else:
        return None
    
    
def add_credits(students,id,credits):
    student=get_student(students,id)
    if not student is None:
        student.credits+= credits
    else:
        students+=[Student(id,credits)]



students=[]
students+=[Student('123456789',0)]
students+=[Student('918298422',0)]
students+=[Student('243343434',0)]
students+=[Student('533534343',0)]
students+=[Student('234324234',0)]
students+=[Student('544454545',0)]
students+=[Student('123311243',0)]
    
    
print(get_student(students,'123456789'))
print(get_student(students,'000000000'))

print(get_credits(students,'123456789'))

add_credits(students,'123456789',4)

print(get_credits(students,'123456789'))


create_hash_table