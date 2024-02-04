# define a function a here

def temp_convert(var):
    try:
        return int(var)
        
    except ValueError as argument:
        print("print this line , argument doesnt contain number \n",argument)
        
        # call above function         

temp_convert("maaz")