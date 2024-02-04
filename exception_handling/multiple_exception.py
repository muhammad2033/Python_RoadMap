try:
    number = 1/0
    print(" zerodivisionerror !",number)
    with open("file.txt","r") as file:
        file = file.read()
except FileNotFoundError as e:
    print("its okey, go for further code!!",e)
    print("yes")
except ZeroDivisionError as zero:
    print(" handled or not!")

else:
    try:
        name = muhammad_maaz
    except Exception as e : #it's handled every error , but we dont need to mention the error's name 
        print("error handled !")      
print("error handled !")      
          
    # we dont have such sort of file , so it will give an error "FileNotFoundError" 
    # similarly , it will be handled by exception 
    