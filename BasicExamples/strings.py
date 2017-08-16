#strings examples
str1='welcome'
str2=' to python world'
#this operation concatenates two strings using + operator
str3=str1+str2
print(str3)

#print first four letters of the string str3 ( it will print from index mentioned below and excludes the last mentioned index
print("Print 0 to 3rd index as mentioned below --> ",str3[0:4])
#print(str3[0:4])

#print last five characters
print("Print last five characters from a given string --> ",str3[-5:])
#print(str3[-5:])

#print whole string except last five characters
print("Print all characters except last five characters --> ",str3[:-5])
# print(str3[:-5])