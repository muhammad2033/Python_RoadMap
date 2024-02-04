# open function 
name = open("readlines.txt",'r+')
print("name of the file:",name.name)

line = name.readlines()
print("line is %s"%(line))


line = name.readlines(22) #nothing
print("line is %s"%(line))

# closed opened file 
name.close()