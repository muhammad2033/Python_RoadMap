                    # method no 1 for reading and writing   


try:
    with open("file.txt","r") as file:
        file = file.read()
except FileNotFoundError as e:
    print("its okey, go for further code!!",e)
    print("yes")
    
    # we dont have such sort of file , so it will give an error "FileNotFoundError" 
    # similarly , it will be handled by exception 
    

                    # method no 2 for reading and writing   
try:
    read=  open("file.txt","r")
    print(read)
except FileNotFoundError:
    print("its okey, go for further code!!")
    print("yes")    
    
            # method no 3 for reading and writing   
try:
    read=  open("file.txt","r")
    print(read)
except Exception as e:
    print("its okey, go for further code!!",e)
    print("yes")        