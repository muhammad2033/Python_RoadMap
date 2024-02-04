# Python bytes()
# In this tutorial, we will learn about the Python bytes() method with the help of examples.

# The bytes() method returns an immutable bytes object initialized with the given size and data.

# Example

message = 'Python is fun'

# convert string to bytes
byte_message = bytes(message, 'utf-8')
print(byte_message)

# Output: b'Python is fun'

# Run Code
# bytes() Syntax
# The syntax of bytes() method is:

# bytes([source[, encoding[, errors]]])
# bytes() method returns a bytes object which is an immutable (cannot be modified) sequence of integers in the range 0 <=x < 256.

# If you want to use the mutable version, use the bytearray() method.

# bytes() Parameters
# bytes() takes three optional parameters:

# source (Optional) - source to initialize the array of bytes.
# encoding (Optional) - if the source is a string, the encoding of the string.
# errors (Optional) - if the source is a string, the action to take when the encoding conversion fails (Read more: String encoding)
# The source parameter can be used to initialize the byte array in the following ways:

# Type	Description
# String	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
# Integer	Creates an array of provided size, all initialized to null
# Object	A read-only buffer of the object will be used to initialize the byte array
# Iterable	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
# No source (arguments)	Creates an array of size 0
# bytes() Return Value
# The bytes() method returns a bytes object of the given size and initialization values.

# Example 1: Convert string to bytes

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

# Run Code
# Output

# b'Python is interesting.'

# Example 2: Create a byte of given integer size

size = 5

arr = bytes(size)
print(arr)

# Run Code
# Output

# b'\x00\x00\x00\x00\x00'

# Example 3: Convert iterable list to bytes

rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)

# Run Code
# Output

# b'\x01\x02\x03\x04\x05'