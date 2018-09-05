#SET OPERATIONS
x=set("Welcome to Python World")
print("\n=================Set allows only unique values=================\n")
print("\nDisplaying Set -->> ",x)

#DEFINE SET DATA TYPE
l = ['s','s','d']

#CONVERT LIST TO SET
g = set(l)

'''
PRINT A SET ( IT REMOVES A DUPLICATE CHARACTERS FROM A LIST
SET IS AN UNORDERED COLLECTION WHICH HAS UNIQUE ELEMENT IN IT
'''
#PRINT SET
print("\n Displaying set after converting from list -->> ",g)

#PRINT LENGTH
print("Set length -->> ",len(g))

employees=["ram","kiran","raj","prem", "ram","kiran"]
print("\nPrinting Employees -->> ",employees,", Employees Length : ",len(employees))
print("\nConverting from list to set\n")
employeeSet = set(employees)
print("Displaying Set values after converting from list -->> ",employeeSet,", Employees Length : ",len(employeeSet))