#OPEN FILE
print("**************Creating file using python**************\n")
f =open('E:/Python_RND/file_operation.txt','w',encoding='utf-8')
print("\n")
print("**************Writing to file using python**************")
#WRITE CONTENTS TO FILE OBJECT
f.write('Hi, this is first line writing using python code')
#Close file after writing
f.close();

#READ A FILE
f = open("E:/Python_RND/file_operation.txt",'r',encoding='utf-8')

#READ first 6 characters
print("Reading first 6 characters from a file")
text = f.read(6)
print(text)
print("")

#PRINT THE CONTENTS OF FILE USING READLINES() method
print("\n")
print("Reading all the lines from a file using python")
print(f.readlines())
f.close()

#APPENDING CHARACTERS TO FILE

f.open("E:/Python_RND/file_operation.txt",'a',encoding='utf-8')
f.write("\n THIS IS MY SECOND LINE")
print("\n****************Printing file after appending characters to a file****************\n")
print(f.readlines())
f.close() 
