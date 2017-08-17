#DETAILS ABOUT CLASSES AND OBJECTS
class Student:
    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first+'.'+last+"@gmail.com"

    def fullname(self):
        return '{} {}'.format(student3.first,student3.last)

#INHERITANCE EXMAPLE
class Dumb(Student):
    pass

dumbStudent = Dumb('Mac','John','209')
print("Name of student after inheriting the student class --> ",dumbStudent.first)
'''
# CREATIION OF OBJECT FOR CLASS
student1 = Student()
student2 = Student()

#defining instance variable for object
student1.first = 'Maqbul'
student1.last = 'Kotwal'
student1.email='maqbul.kotwal@gmail.com'
student1.marks=450

student2.first="Raj"
student2.last = "Singh"
student2.email = "raj.singh@gmail.com"
student2.marks = 490

#PRINT EMAIL of both the objects
print(student1.email)
print(student2.email)
'''
student3 = Student('Rohan','Pathak','480')
print(student3.marks)
print(student3.email)

print("Full name --> ",student3.fullname())

print("Display object as dictionary --> ",student3.__dict__)

print("Display Student as Dictionary --> ",Student.__dict__)
stuDict = student3.__dict__

print("Student dictionary values --> ",stuDict.values())
print("Student dictionary keys --> ",stuDict.keys())

print("Student by key name --> ", stuDict['first'])