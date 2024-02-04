import os ,sys 

# open function 
name = os.open("dup2.txt",os.O_RDWR|os.O_CREAT)

# write one  string using duplicate name 


line =  "this is test"
#string needs to be converted into byte object

b = str.encode(line )

os.write(name, b ) 

# now duplicate this file   descriptor as 1000
name2 = 1000

os.dup2(name, name2 )

# now read this file from the beginning using name2
os.lseek(name2,0,0 )

line = os.read(name2, 100)
str = line.decode()

print(" read string   is: ",str)

# close opened file  
os.closerange(name,name2)

print("close all file successfully ")