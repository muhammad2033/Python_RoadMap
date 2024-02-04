import os, sys
# Open a file
path = "d://python3//foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )
# Close opened file
os.close( fd )
# Now create another copy of the above file.
dst = "d://project// foo.txt"
os.link( path, dst)
print ("Created hard link successfully!!")
