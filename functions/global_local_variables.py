total = 5    #this is a global variable 

def sum(a,b):     #function definition  
    
    total = a + b   # this is a local variable 
    return total 
print("total for inside is :",total)
    
    

sum(10,20)  #function call

print("total for outside is :",total )