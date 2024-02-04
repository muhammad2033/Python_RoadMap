# open function 
name = open("truncate.txt","r+")
print("name of the file :",name.name)

line = name.readline()
print("read line : %s"%(line))

# truncate means the to shorten something

name.truncate(14)  
line = name.readlines()
print("read line : %s"%(line))

# close the opened file 

name.close()