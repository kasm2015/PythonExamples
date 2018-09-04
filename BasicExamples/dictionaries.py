#DICTIONARIES EXAMPLES
westeros={'cersei':'lannister','daenerys':'targaeyn','sansa':'stark'}
print("\nDisplaying dictionary keys:values : ",westeros,"\n")

#if you want to change the certain value of a particular key in dictionary
westeros['daenerys']='dothraki'
print("Dictionary after remodification : ",westeros,"\n")

#if you want to view just the keys
print("Print dictionary keys : ",westeros.keys(),"\n")

#if you want to view just the values
print("Print dictionary values : ",westeros.values(),"\n")

#print the value by specifying key
print("Print dictionary value by key : ",westeros['cersei'],"\n")

#if you want to delete by its key name
del westeros['cersei']
#print it the updated dictionary
print("Dictionary after deleting  : ",westeros,"\n")

#reinitialize the dictionary
westeros={'Syed':'Kotwal'}
print("Dictionary values after reinitializing : ",westeros,"\n")
del westeros['Syed']
print("Dictionary after deleting key --> ",westeros,", Dictionary Length : ", westeros.__len__())

#CHECK THE TYPE OF OBJECT
print("Check type of dictionary object --> ",type(westeros),"\n")

customerdictionary = {'cust1':'ABC','cust2':'XYZ','cust3':'PQR'}

print("Customers Keys : ", customerdictionary.keys(),"\n")
print("Customers Values : ", customerdictionary.values(),"\n")
print("Total Customers : ",customerdictionary.__len__(),"\n")
