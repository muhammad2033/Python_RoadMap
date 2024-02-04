# Decorating Functions with Parameters

# The above decorator was simple and it only worked with functions that did not have any parameters.
# What if we had functions that took in parameters like:

# def add (a , b):
#     return a + b 

# This function has two parameters, a and b. We know it will give an error if we pass in b as 0.

# Now let's make a decorator to check for this case that will cause the error.

def make_pretty(func):
    def inner(a, b):
        print(f" let's divide {a} by {b} !")
        try:
            if b==0:
                print(a/b)
        
        except Exception as e:
                print("this should not  have been given , gives error  ", e)
                print('yes')
         
                return 
        return func(a ,b)
    
    return inner

@make_pretty
def divide(a , b):
    print(a/b)
    

divide(2,5)            

divide(2,0)

# Here, when we call the divide() function with the arguments (2,5), the inner() function defined in the smart_divide() decorator is called instead.

# This inner() function calls the original divide() function with the arguments 2 and 5 and returns the result, which is 0.4.

# Similarly, When we call the divide() function with the arguments (2,0), the inner() function checks that b is equal to 0 and /prints an error message before returning None.     


# own practice

def own(func):
    def inner(a,b, c):
        print(f"let's add the {a} with {b} and then divide {a} , {b} by {c} ")
        if c == 0:
            print(" there is an error")
            return
        return func(a,b,c)

    return inner

@own
def divide(a,b,c):
    print((a+b)/c)

divide(2,4,6)
divide(5,6,0)