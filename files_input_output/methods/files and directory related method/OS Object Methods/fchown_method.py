import os, sys, stat

# Now open a file "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )

# Set the user Id to 100 for this file.
os.fchown( fd, 100, -1)

# Set the group Id to 50 for this file.
os.fchown( fd, -1, 50)

print ("Changed ownership successfully!!")
# Close opened file.

os.close( fd )
