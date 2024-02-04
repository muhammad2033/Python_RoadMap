# open function
name = open("writelines.txt","r+")
print("name of the file :",name.name )

seq = ['\n this is 6th line \n','this is 7th line']

# write sequences of the lines at the end 
name.seek(0,2)

line = name.writelines(seq)

# now read complete  file from beginning 
name.seek(0,0)

for index in range(8):
    line = next(name)
    print("read line %d - %s"%(index ,line ))
    
# now close the opened file
name.close()