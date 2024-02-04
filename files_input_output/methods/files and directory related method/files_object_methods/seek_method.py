# open function 
name = open("seek.txt","r+")
print("name of the file",name.name)

line = name.readlines() # that will be a list of lines 
print("read line is : %s "%(line))

# again set the pointer to the beginning 

name.seek(0,2) #that will be an empty
#when seek is (0,0), then will print a line
 
line = name.readline() #that will be one line
print("read line is : %s"%(line))

# close opened file 
name.close()