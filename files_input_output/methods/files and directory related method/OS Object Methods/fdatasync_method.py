import os, sys
# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# Write one string
line="this is test" 
# string needs to be converted byte object
b=str.encode(line)
os.write(fd, b)
# Now you can use fdatasync() method.
# Infact here you would not be able to see its effect.
os.fdatasync(fd)
# Now read this file from the beginning.
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
line = os.read(fd2, 100)
str=line.decode()
print ("Read String is : ", str)
# Close opened file
os.close( fd )
print ("Closed the file successfully!!")
