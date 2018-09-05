#LIST EXAMPLES
knights=["ser jaime","ser barristan","ser rodrick"]

#find the length of the list
print("\n===================List Examples===================")
print("\nKnights list --> ",knights)
print("\nLen of knights list is --> ",len(knights))

#add more items in list, since lists are mutable, whenever you add new item into the list, it add at the last index
print("\nFor adding value to list use append method")
knights.append("Lady brienne")

#print the list after adding more items
print("\nList after adding more items -->> ",knights)

#if you want to add item at first index then
print("\nUse insert method for inserting value to specific location in a list ")
knights.insert(1,"ser podrick payne")
print("\nAdding item at index 1 -->> ",knights)

#adding item at index 0
knights.insert(0,"Syed Maqbul")
print("\nAdding item at index 0 -->> ",knights)

print("\nList updated size : ",len(knights))
print("\nAdding item to index greater than actual lenght to a list")
knights.insert(len(knights)+1,"Kotwal")

print("\nAfter Adding item to index greater than actual lenght to a list -->> ",knights)
#TUPLES EXAMPLES ( tuples are immutable)
print("\n===================Tuples examples===================\n")
houses=('stark','tyrell','lannister')
print("Displaying tuples -->> ",houses)
#if you try add items to tuples it throws an error ( AttributeError: 'tuple' object has no attribute 'append' )
#houses.append('bolton')

#You can changes values in tuples by following way, convert tuple into list
house1 = list(houses)
house1.append('bolton')
print(house1)

#if you want convert the list into tuples back then
houses = tuple(house1)
