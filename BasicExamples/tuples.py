#DEFINIG A TUPLE
task=('tea','milk','coffee')

#PRINT TUPLE
print(task)

#Update a tuple ( NOT POSSIBLE)
'''
TypeError: 'tuple' object does not support item assignment
'''
#task[0]='new'

#PRINT THE LENGTH OF TUPLE
print("Length of a tuple --> ",len(task))

#PRINT AN ELEMENT FROM A TUPLE
w = task[2]
print("PRINT AN ELEMENT OF A TUPLE --> ",w)

#PRINT A PART OF THE TUPLE
print("Print part of the values from a tuple --> ",task[0:2])

#Concatenate tuples
tup1 = ('coke','pepsi')

print("Concatenation of two tuples --> ",task+tup1)

#Print tuple multiple times
print(task*2)