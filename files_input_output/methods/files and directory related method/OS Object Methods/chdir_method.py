import os

path = "d:\\project" #change  path for window

# now change the directory

os.chdir(path)

# check current working directory 

retval = os.getcwd()

print("directory is successfully changed %s"%(retval))