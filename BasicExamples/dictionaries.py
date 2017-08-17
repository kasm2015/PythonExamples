#DICTIONARIES EXAMPLES
westeros={'cersei':'lannister','daenerys':'targaeyn','sansa':'stark'}
print(westeros)
#if you want to change the certain value of a particular key in dictionary
westeros['daenerys']='dothraki'
print(westeros)

#if you want to view just the keys
print(westeros.keys())

#if you want to view just the values
print(westeros.values())

#print the value by specifying key
print(westeros['cersei'])

#if you want to delete by its key name
del westeros['cersei']
#print it the updated dictionary
print(westeros)

#reinitialize the dictionary
westeros={'Syed':'Kotwal'}
print(westeros)
del westeros['Syed']
print("Dictionary after deleting key --> ",westeros)

#CHECK THE TYPE OF OBJECT
print("Check type of object --> ",type(westeros))