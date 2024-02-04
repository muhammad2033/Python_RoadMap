# Python Decorators
# As mentioned earlier, A Python decorator is a function that takes in a function and returns it by adding some functionality.

# In fact, any object which implements the special __call__() method is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

# Basically, a decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
    def inner():
        print(" its been decorated!")
        func()
        
    return inner 

def ordinary():
    print("i am a programmer")
    
# Here, we have created two functions:

# ordinary() that prints "I am ordinary"

# make_pretty() that takes a function as its argument and has a nested function named inner(), and returns the inner function.

# We are calling the ordinary() function normally, so we get the output "I am ordinary". Now, let's call it using the decorator function.       


def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behaviour to decorated function 
        
        print(" its been decorated!")
        # calling the original function now 
        
        func()
    # return the inner function 
    
    return inner 

# define the ordinary function 

def ordinary():
    print("i am a programmer")
    
# decorate the ordinary function 

decorate_func = make_pretty(ordinary)

# call the decorate funcion 
decorate_func()    

# Output

# I got decorated

# I am ordinary

# In the example shown above, make_pretty() is a decorator. Notice the code,

# decorated_func = make_pretty(ordinary)

# We are now passing the ordinary() function as the argument to the make_pretty().

# The make_pretty() function returns the inner function, and it is now assigned to the decorated_func variable.

# decorated_func()

# Here, we are actually calling the inner() function, where we are printing