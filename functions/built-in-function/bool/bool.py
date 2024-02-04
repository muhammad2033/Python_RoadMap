# Python bool()
# In this tutorial, you will learn about the Python bool() method with the help of examples.

# The bool() method takes a specified argument and returns its boolean value.

# Example-

test = 1

# returns boolean value of 1
print(test, 'is', bool(test))

# Output: 1 is True
# Run Code

# bool() Syntax
# The syntax of bool() is:

# bool(argument)
# bool() Parameter
# The bool() method takes in a single parameter:

# argument - whose boolean value is returned
# bool() Return Value
# The bool() method returns:

# False - if argument is empty, False, 0 or None
# True - if argument is any number (besides 0), True or a string
# Example 1: Python bool() with True Arguments


test = 254
# bool() with an integer number
print(test, 'is', bool(test))

test1 = 25.14
# bool() with a floating point number
print(test1, 'is', bool(test1))

test2 = 'Python is the best'
# bool() with a string
print(test2, 'is', bool(test2))

test3 = True
# bool() with True
print(test3, 'is', bool(test3))


# Run Code
# Output

# 254 is True
# 25.14 is True
# Python is the best is True
# True is True

# In the above example, we have used the bool() method with various arguments like integer, floating point numbers, and string.

# Here, the method returns True values for arguments like 25, 25.14, 'Python is a String', and True.

# Example 2: bool() with False Arguments


test = []
# bool() with an empty argument
print(test, 'is' ,bool(test))

test1 = 0
# bool() with zero
print(test1, 'is' ,bool(test1))

test2 = None
# bool() with none
print(test2, 'is' ,bool(test2))

test3 = False
# bool() with False
print(test3, 'is' ,bool(test3))


# [] is False
# 0 is False
# None is False
# False is False