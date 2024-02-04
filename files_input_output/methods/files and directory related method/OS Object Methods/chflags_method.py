import os

path = "/tmp/foo.txt"
# Set a flag so that file may not be renamed or deleted.

flags = os.O_APPEND

retval = os.chflags( path, flags)

print ("Return Value: %s" % retval)
