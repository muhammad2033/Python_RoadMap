import os, sys

# Open a file

fd = os.open( "closerange.txt", os.O_RDWR|os.O_CREAT )
# Write one string

line="this is test" 
# string needs to be converted byte object

b=str.encode(line)
os.write(fd, b)

# Close a single opened file
os.closerange( fd, fd)

print ("Closed all the files successfully!!")