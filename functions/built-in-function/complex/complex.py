# Python complex()
# The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.

# The syntax of complex() is:

# complex([real[, imag]])
# complex() Parameters
# In general, complex() method takes two parameters:

# real - real part. If real is omitted, it defaults to 0.
# imag - imaginary part. If imag is omitted, it defaults to 0.
# If the first parameter passed to this method is a string, it will be interpreted as a complex number. In this case, the second parameter shouldn't be passed.

# Return Value from complex()
# As suggested by the name, complex() method returns a complex number.

# If the string passed to this method is not a valid complex number, ValueError exception is raised.

# Note: The string passed to complex() should be in the form real+imagj or real+imagJ

# Example 1: How to create a complex number in Python?

z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)


# Run Code
# Output

# (2-3j)
# (1+0j)
# 0j
# (5-9j)

# Example 2: Create complex Number Without Using complex()
# It's possible to create a complex number without using complex() method. For that, you have to put 'j' or 'J' after a number.

a = 2+3j
print('a =',a)
print('Type of a is',type(a))

b = -2j
print('b =',b)
print('Type of b is',type(a))

c = 0j
print('c =',c)
print('Type of c is',type(c))

# Run Code
# Output

# a = (2+3j)
# Type of a is <class>
# b = (-0-2j)
# Type of b is <class>
# c = 0j
# Type of c is <class>