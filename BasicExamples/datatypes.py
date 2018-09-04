#boolean examples
'''multi line commments
can be written like this'''

num=[1,2,3,4,5]
y=3 in num #check 3 is present in num list
z=45 in num
if(y):
    print("y value present")
if(z):
    print("z value present")
else:
    print("z value not present")
print("Y value : ",y)
x= 6 in num #check 6 is present un num list
print("X value : ",x)

#numbers examples
print("Value of 5**3 : ",5**3)
print("Value of 32//3 : ",32//3)


#integer
a = 10
#complex data type
b = 2+8j
print("value of b : ",b)

#Float data type
c = 2.35
print("Value of c : ",c)

'''
Type convertion
1. convert integer to float
2. convert float to integer
'''
d = float(a)
print("Conversion of int to float --> ",d)

e = int(c)
print("Conversion of float to int --> ",e)

