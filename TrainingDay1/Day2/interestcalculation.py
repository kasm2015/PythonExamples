'''
    script name     : interestcalculation.py
    Author          : Syed Maqbul
    Date            : 06-Dec-2018
    Description     : Write a program to enter principl amount,Rate of interest, time as
                      input values from keyboard and calclate simple interest.
                      Note : Formula I = PTR/100
'''
principal=int(input("Enter principal amoutn         : "))
rateOfInterest=int(input("Enter rate of interest    : "))
time=int(input("Enter time                          : "))

simpleInterest = (principal * rateOfInterest * time)/100
print("Simple Interest for the principal amount for tenure of ",time," is ",simpleInterest)