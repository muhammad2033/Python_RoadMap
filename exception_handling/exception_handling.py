try:
    name = open("exception.txt","w")
    name.write("this is the program for exception handling!! ")
   
except IOError:
    print("error:can\'t find file  or read data")

else:
    print(" written  content  it the file successfully!")
    name.close()
        
        
        
try:
    name = open("exception.txt","r")
    name.write("this is the program for exception handling!! ")
   
except IOError:
    print("error:can\'t find file  or read data")

else:
    print(" written  content  it the file successfully!")
    name.close()
                