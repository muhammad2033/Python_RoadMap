# open function 

name = open("text.txt","wb+") #wb means that writing in binary format 
print("name of the file:",name.name)

print("closed or not : ",name.closed) #false,coz the file isn't closed

print("opening mode: ",name.mode) #mode's name

name.close()

print("closed or not : ",name.closed) #true,coz the file is clossed 

