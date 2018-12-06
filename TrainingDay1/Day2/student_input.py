'''
    Script name     : student_input.py
    Author          : Syed Maqbul Hussain
    Date            : 04-Dec-2018
    Description     : Write a program to enter student name,sub1 marks ,sub2 marks,sub3 marks
                      as input calulate total marks and avg.

'''
studentName = input("Enter student name : \n")
s1_Marks    = int(input("Enter subject1 marks : \n"))
s2_Marks    = int(input("Enter subject2 marks : \n"))

print("Student Name         : ",studentName)
print("Subject 1 Marks      : ",s1_Marks)
print("Subject 2 Marks      : ",s2_Marks)

total=s1_Marks + s2_Marks
print("Total Marks          : ",total)
