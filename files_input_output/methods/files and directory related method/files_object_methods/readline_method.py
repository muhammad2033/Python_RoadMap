# open function 
name = open("readline.txt","r+")
print("name of the file:",name.name)

line = name.readline() #by defualt only one  line will be read and printed
print("read line is %s"%(line))


line = name.readline(6) # upto 6 index ,it will be read
print("read line is %s"%(line))
      
# closed opened file 
name.close()    

# readline  is used to read a single line   