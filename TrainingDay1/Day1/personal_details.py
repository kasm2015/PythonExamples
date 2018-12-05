'''
Script name : assignment_29Nov2018.py
Date : 29-Nov-2018
Author : Syed Maqbul

'''
#Personal Details declaration
name='Syed Maqbul'
age =30
gender='male'
salary =200000
city='bangalore'
email='syedmaqbul.corptrainer2016@gmail.com'
mobile=7019593863

#Variable declartion in python
print("1. What are the rules of variables declaration in python?")
print("************Variable Declaration in Python**********")
print("Rules of Declaring variables in Python")
print("1. Variable name should always start with either [a-z] or [A-Z] or _ (underscore)")
print("Valid variables are : abc,abc123, ABC846, _ABC")
print("2. Must not contain any special characters !, @,#,$,%,^,&,*,(,)")
print("Invalid variables are : a&=20, b^=30")
print("****************************************************\n")

#Which of the following are valid in python?
print("2. Which of the following are valid in python")
print("*****Which of the Following are valid in python*****")
print("123accnum = 123124 -->> Invalid syntax")
print("accnum = 1234325   -->> Valid syntax")
print("sal$ = 12000       -->> Invalid syntax")
print("for = 1234         -->> Invalid syntax")
print("gender='male'      -->> Valid syntax")
print("_name='SYED'       -->> Valid syntax")
print("a=true             -->> Invalid syntax")
print("b=False            -->> Valid syntax")
print("****************************************************\n")

#Swap values of 2 variables
print("3. Write a program to swap values of 2 variables")
print("*******************Swap 2 Numbers*******************")
a = 10
b = 20
print("Before swapping : ")
print("A : ",a," & B : ",b)
print("Swapping 2 variables")
a,b=b,a
print("After swapping :")
print("A : ",a," & B : ",b)
print("****************************************************\n")

#Printing personal details
print("4. Writa a program to print self introduction details")
print("******************Personal Details******************")
print('Name   : ',name,'\nAge    : ',age,'\nGender : ',gender,
      '\nSalary : ',salary,'\nCity   : ',city,'\nEmail  : ',email,
      '\nMobile : ',mobile);

print("****************************************************\n")



