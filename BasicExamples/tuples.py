#DEFINIG A TUPLE
task=('tea','milk','coffee')

#PRINT TUPLE
print("\nPrint task in a tuple -->> ",task,", Length : ",len(task))

#Update a tuple ( NOT POSSIBLE)
'''
TypeError: 'tuple' object does not support item assignment
'''
#task[0]='new'

#PRINT THE LENGTH OF TUPLE
print("\nLength of a tuple --> ",len(task))

#PRINT AN ELEMENT FROM A TUPLE
w = task[2]
print("\nPrint a tuple at index 2 --> ",w)
#Below code returns IndexError : tuple index out of range
#print("\nPrint a index which is not available : ",task[len(task)+1])

#PRINT A PART OF THE TUPLE
print("\nPrint part of the values from a tuple --> ",task[0:2])

#Concatenate tuples
tup1 = ('coke','pepsi')

print("\nConcatenation of two tuples --> ",task+tup1)

#Print tuple multiple times
print(task*2)