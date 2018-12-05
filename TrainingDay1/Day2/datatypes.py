'''
Author      : Syed Maqbul
Date        : 04-Dec-2018
Description :
Python Datatypes
==========================================================================
A datatype represents the type of data stored into a variable or memory.

Buitin datatypes -- Already available in python
1. Built in datatypes :

 * None Type
 * Boolean Type
 * Numaric Types --> int,float,complex
 * Sequences     --> str,bytes,bytearray,list,tuple,range
 * Sets          --> set,frozenset
 * Mappings      --> dict
'''

#None datatype
print("None data type ->",type(None));

def calc():
    a=10;
    b=20;
    c=a+b;

#When you call calc() method, its returns None
print("Calling calc() -> ",calc());
print("Type of calc() -> ",type(calc()))

#Storing the result to res variable
res = calc();
print("Calc() method results is stored, checking its type -> ",type(res));
if(res==None):
    print("does not return any values")

'''
Numaric dataypes :
--------------------
1. int
2. float
3. complex
'''
#1. int datatype
a=0;
print("a variable type -> ",type(a));

a = 223.345
print("Float type -> ",type(a))

#Converting the datatype explicitly :
x = 23
print("X ->",x," & type -> ",type(x));
b = float(x)
print("After converting x to float, x -> ",b," & type -> ",type(b))

'''
Complex Datatype
  complex number is number that is written in the form of a+bj or a+bJ
   a : real part
   b : imaginary part
'''
a = 1+2j
b = 2+3j
c = a + b
print("Complex value of c -> ",c)

c = 1+2j
d = 1-2j
#multiplication of two numbers
res = c * d
print("Value of res -> ",res)


'''
Sequences in Python :
--------------------
 A sequence represents a group of elements or items.

 eg : group of integer numbers will form seqence

 There are six types of sequences in python :
 1. str
 2. bytes
 3. bytearray
 4. list
 5. tuple
 6. range

str datatype :

  * str represents string datatype.
  * string represents group of characters
  * string enclosed in single quotes or double quotes('',"")
  * string can also be represent in """ or '' if assign to variable then string otherwise it would be comment only)

'''
word = "Welcome"
print("Str value -> ",word)

word = "'Welcome'"
print(word)

word = """welcome"""
print(word)

#for='Welcome to python world!!!'
#SyntaxError: invalid syntax (for is key word, variable name should not be key word)


#Printing a string literal
name = "Syed-Maqbul"

# Prints complete string
print(name)

# Prints first character of the string
print (name[0])

# Prints characters starting from 3rd to 5th
print (name[2:5])

# Prints string starting from 3rd character
print (name[2:])

# Prints string two times
print (name * 2)

# Prints concatenated string
print(name + " Kotwal")

