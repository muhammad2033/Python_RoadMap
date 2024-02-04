# open function 
name = open("write.txt","r+")
print("name of the file :",name.name)

str = "this a new line which i wanna print at the end"

# write a line at the end  
name.seek(0,2)
line = name.write(str)

# now read complete files from  the beginning  
name.seek(0,0)
for index in range(6):
    
    line = next(name)
    print("read line %d : %s"%(index,line))
# close the opened file  
name.close()