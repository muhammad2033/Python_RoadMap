                                            # Return a Function as a Value
                                        
def greeting(name):
    def hello():
        return "helo",name,"!!"
    return hello

result = greeting("maaz")
print("result:",result())

# here result is become the inisde fiunction and greeting is outside 


# In the above example, the return hello statement returns the inner hello() function. This function is now assigned to the result variable.

# That's why, when we call result() as a function, we get the output.


# extra practice 

def calling(ally):
    def salute():
        return "salute for " ,ally ," khan "
    return salute 

result = calling ("maaz")
print("result for calling name :",result())

# if we print result only , it will consider only the object and if put parentheses after result , then it will be considering as a function 