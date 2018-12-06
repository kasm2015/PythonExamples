'''
    script name     : employeedetails.py
    Author          : Syed Maqbul
    Description     : Write a program to read employee data from keyboard and Print.
                      Note : employee data contains empno,empname,empsal,empaddress
'''
#Enter employee information
empno = int(input("Enter employee number        : \n"))
empname =input("Enter employee name          : \n")
empsal = float(input("Enter employee salary        : \n"))
empaddress = input("Enter employee address       : \n")

#Printing Employee Information
print("Employee Name        : ",empname)
print("Employee Number      : ",empno)
print("Employee Salary      : ",empsal)
print("Employee Address     : ",empaddress)