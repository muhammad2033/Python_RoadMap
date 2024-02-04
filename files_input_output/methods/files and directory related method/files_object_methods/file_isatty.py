# open a file    

name = open("foo.txt","wb")
print("name of the file :",name.name)

ret = name.isatty()
print("return the value :",ret )

# close the opened file 
name.close()