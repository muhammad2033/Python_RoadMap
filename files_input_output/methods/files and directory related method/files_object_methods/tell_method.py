# open function

name = open("tell.txt","r+")
print("name of the file :",name.name) 

line = name.readline()
print("read line : %s"%(line))

tell = name.tell()
print("current position is:",tell)


# close the opened file   
 
name.close()