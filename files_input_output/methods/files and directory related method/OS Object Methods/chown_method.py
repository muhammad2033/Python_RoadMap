import os ,sys 

# assuming \tmp\foo.txt\ exists 

# to set owner id 100  followind has to be done                

os.chown("/tmp/foo.txt",100,-1)

print("change owner successfully!!     ")