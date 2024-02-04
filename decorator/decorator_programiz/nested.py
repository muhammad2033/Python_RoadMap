                                    # Python Decorators
# 
# In this tutorial, we will learn about Python Decorators with the help of examples.



# n Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

# The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

# Prerequisites for learning decorators
# Before we learn about decorators, we need to understand a few important concepts related to Python functions. Also, remember that everything in Python is an object, even functions are objects.

                                # Nested Function

# We can include one function inside another, known as a nested function. For example,

def outer(x):
    def inner(y):
        return x+y
    return inner

add_inner= outer(6)
result= add_inner(7)
print("nested_funtion",result)

# Here, we have created the inner() function inside the outer() function.

# here add_inner becomes an inner function


# extra practice       

def extra (x):
    def inner(y):
        return x*y
    return inner 

inner_func = extra(7)
result = inner_func(9)
print("result for multiplication :",result)