import os, sys, stat

# Now open a file "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )

# set a file execute by group 

os.fchmod( fd, stat.S_IXGRP)

# Set a file write by others.
os.fchmod(fd, stat.S_IWOTH)

print ("Changed mode successfully!!")

# Close opened file.
os.close( fd )