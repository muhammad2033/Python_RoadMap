import os, sys
# Open a file
fd = os.open( "write.txt", os.O_RDWR|os.O_CREAT )
# Write one string
line="this is test" 
# string needs to be converted byte object
b=str.encode(line)
ret=os.write(fd, b)
# ret consists of number of bytes written to f1.txt
print ("the number of bytes written: ", ret)
# Close opened file
os.close( fd)
print ("Closed the file successfully!!")