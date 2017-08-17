#OPEN FILE
f =open('C:/Maqbul Files/test.txt','w',encoding='utf-8')

#WRITE CONTENTS TO FILE OBJECT
f.write('Hi this is first line')
#Close file after writing
f.close();

#READ A FILE
f = open("c:/Maqbul Files/test.txt",'r',encoding='utf-8')

#READ first 6 characters
#text = f.read(6)
#print(text)

#PRINT THE CONTENTS OF FILE USING READLINES() method
print(f.readlines())
f.close()

#APPENDING CHARACTERS TO FILE
'''
f.open("c:/Maqbul Files/text.txt",'a',encoding='utf-8')
f.write("\n THIS IS MY SECOND LINE")
print("Printing file after appending characters to a file")
print(f.readlines())
f.close() 
'''