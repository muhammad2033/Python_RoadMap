# Chaining Decorators in Python

# Multiple decorators can be chained in Python.

# To chain decorators in Python, we can apply multiple decorators to a single function by placing them one after the other, 

# with the most inner decorator being applied first.

def star(func):
    def inner(*args,**kwargs):
        print("*" * 15)
        func(*args,**kwargs)
        print("*" * 15)
        
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print("%" * 15)
        func(*args,**kwargs)
        print("%" * 15)
        
    return inner

@star    #printer = star()
@percent
def printer():
    print()
    
printer() 


# Output

# ***************
# %%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%
# ***************


# The above syntax of,

# @star
# @percent
# def printer(msg):
#     print(msg)
    
# is equivalent to

# def printer(msg):
#     print(msg)
# printer = star(percent(printer))

# The order in which we chain decorators matter. If we had reversed the order as,

# @percent
# @star
# def printer(msg):
#     print(msg)

# The output would be:
    

# %%%%%%%%%%%%%%%
# ***************
# Hello
# ***************
# %%%%%%%%%%%%%%%   