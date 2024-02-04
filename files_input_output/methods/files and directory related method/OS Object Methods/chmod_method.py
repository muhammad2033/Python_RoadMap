import os ,sys ,stat 

# assuming /tmp/read.txt exists , set a file executed by  group 

os.chmod("/tmp/read.txt",stat.S_IXGRP)

# set  a file  write by group 

os.chmod("/tmp/write.txt",stat.S_IWOTH)

print("changed mode successfully!!") 