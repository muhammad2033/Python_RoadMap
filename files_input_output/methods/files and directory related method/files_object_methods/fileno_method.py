#open function 

name = open("foo.txt","wb")
print("name of the file :",name.name)

fib = name.fileno(12)
print(" file decriptor:",fib)

# close opened file  

name.close()