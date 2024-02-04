def changeme(mylist):  #function definition 
    
    "this is a simple function program!"
    
    print("value inside a function before changing= ",mylist)
    
    mylist[2]=60   #updation
    
    print("value inside the function after changing= ",mylist)
    
    return

mylist = [20,40,50,80] 

changeme(mylist)  #function calling     

print("value outside the function! =",mylist )

