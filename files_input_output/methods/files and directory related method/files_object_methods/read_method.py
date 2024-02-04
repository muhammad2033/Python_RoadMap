# open function   
name = open("read.txt","r+")
print("name of the file :",name.name)

line = name.read(11)
# line = name.read() #default all lines will be printed and read

print("line no  %s"% (line))
        
name.close()        