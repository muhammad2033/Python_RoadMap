                        # membership operator 
                        
a = 30 
b = 38 
list = [2 , 3,   4, 6  ,7,8]

if (a in list):
    print("yes ")
else:
    print("no")
    
if (a not in list):
    print("no, it isnt given")
    
else:
    print("yes")        


                            # identity operator 
a = 30 
b = 38 

print(a, " :" ,id(a), "and ",b,  ":", id(b))

if (a is b):
    print("hello")         
else:
    print("no")     
    
if (a is not b):
    print("yell")
else:

    print("help")        
    
    
if (id(a)==id(b)): #identity oeprator
    print("yellng ")
else:

    print("helping")        
                      
                      
                      
                     