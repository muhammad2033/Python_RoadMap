import os, sys

# Open a file
fd = os.open( "close.txt", os.O_RDWR|os.O_CREAT )

# Write one string
line="this is test" 

# string needs to be converted byte object
b=str.encode(line)

os.write(fd, b)
# Close opened file

os.close( fd )
print ("Closed the file successfully!!")
