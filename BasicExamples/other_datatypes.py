#LIST EXAMPLES
knights=["ser jaime","ser barristan","ser rodrick"]

#find the length of the list
print("Len of knights list is --> ",len(knights))

#add more items in list, since lists are mutable, whenever you add new item into the list, it add at the last index
knights.append("Lady brienne")

#print the list after adding more items
print(knights)

#if you want to add item at first index then
knights.insert(1,"ser podrick payne")
print(knights)

#adding item at index 0
knights.insert(0,"Syed Maqbul")
print(knights)

#TUPLES EXAMPLES ( tuples are immutable)
houses=('stark','tyrell','lannister')

#if you try add items to tuples it throws an error ( AttributeError: 'tuple' object has no attribute 'append' )
#houses.append('bolton')

#You can changes values in tuples by following way, convert tuple into list
house1 = list(houses)
house1.append('bolton')
print(house1)

#if you want convert the list into tuples back then
houses = tuple(house1)
