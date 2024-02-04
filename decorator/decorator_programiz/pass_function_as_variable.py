# We can pass a function as an argument to another function in Python. For Example,
def add(x,y):
   return x+y

def multi(x,y):
       return x*y

def calculate(func, x , y):
    return func(x,y) 

result = calculate(add, 4,5)
print("adding two variables:", result)


result = calculate(multi, 4,5)
print("multiplying two variables:", result)

# In the above example, the calculate() function takes a function as its argument. While calling calculate(), we are passing the add() function as the argument.

# In the calculate() function, arguments: func, x, y become add, 4, and 6 respectively.

# And hence, func(x, y) becomes add(4, 6) which returns 10.



# extra prartice 

def extra(x,y):
    return x +y 

def calculation(func, x, y):
    return func(x, y)

result = calculate(extra,6,7)
print("result for practice",result)
