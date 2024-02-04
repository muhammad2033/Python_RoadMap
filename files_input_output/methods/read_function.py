#open function 

file = open ("read.txt","r")
str = file.read()
print("the read.txt file is:",str)

#closing the opened file 
file.close()


# we create binary format too,we will put the number in the read function ,like(12)
#  Open a file

fo = open("read.txt", "r+")

str = fo.read(10)
print ("Read String is : ", str)

# it prints the string upto 10 index

# Close opened file
fo.close()