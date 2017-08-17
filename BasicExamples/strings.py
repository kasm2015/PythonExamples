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

#STRING LENGTH
print("Print length of a string --> ",len(str1))

#LOCATE A PARTICULAR CHARACTER IN A STRING
print("Locate a char in a string --> ",str1.index('w'))

#COUNT THE NO OF OCCURANCES A CHARACTER HAS
print('No of occurances for the character --> ',str1.count('o'))

#PRINT A PART OF THE STRING
print("PRINT PART OF THE STRING --> ",str1[0:3])

#REVERSE A STIRNG
print("Reverse a string --> ",str1[::-1])

#UPPER CASE
print("CONVERT STRING TO UPPER CASE --> ",str1.upper())

#CHECK IF STRING IN UPPER CASE
print("IS STRING UPPER --> ",str1.isupper())

#LOWER CASE
print("convert string to lower case --> ",str1.upper().lower())

#CHECK IF STRING IS LOWER CASE
print("is string lower --> ",str1.islower())