# open the function is here 

file = open("text.txt","r+")
str = file.read()
print("the reading string is :",str)

# check the current position 

position = file.tell()
print("the current file  position is :",position)

# tell retruns the total length of the indices of string

# reposition pointer  at the beginning the of file 

position = file.seek(0,2)
str = file.read()

print("again the reading string is :",str)

#close opened file 

file.close()
