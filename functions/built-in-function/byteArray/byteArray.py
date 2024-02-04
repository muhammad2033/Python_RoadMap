# Python bytearray()
# In this tutorial, we will learn about the Python bytearray() method with the help of examples.

# The bytearray() method returns a bytearray object which is an array of the given bytes.

# Example


prime_numbers = [2, 3, 5, 7]

# convert list to bytearray

byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')
# Run Code
# bytearray() Syntax
# The syntax of bytearray() method is:

# bytearray([source[, encoding[, errors]]])
# bytearray() method returns a bytearray object (i.e. array of bytes) which is mutable (can be modified) sequence of integers in the range 0 <= x < 256.
# bytearray is a key word 


# If you want the immutable version, use the bytes() method.

# bytearray() Parameters
# bytearray() takes three optional parameters:

# source (Optional) - source to initialize the array of bytes.
# encoding (Optional) - if the source is a string, the encoding of the string.
# errors (Optional) - if the source is a string, the action to take when the encoding conversion fails (Read more: String encoding)
# The source parameter can be used to initialize the byte array in the following ways:

# Type	Description
# String	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors

str = "maaz is a programmer"
print(str.encode())

# Integer	Creates an array of provided size, all initialized to null
# Object	A read-only buffer of the object will be used to initialize the byte array
# Iterable	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
# No source (arguments)	Creates an array of size 0.
# bytearray() Return Value
# The bytearray() method returns an array of bytes of the given size and initialization values.

# Example 1: Array of bytes from a string

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

# Run Code

# Output

# bytearray(b'Python is interesting.')

# Example 2: Array of bytes of given integer size

size = 5

arr = bytearray(size)
print(arr)

# Run Code
# Output

# bytearray(b'\x00\x00\x00\x00\x00')

# Example 3: Array of bytes from an iterable list

rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)

# Run Code
# Output

# bytearray(b'\x01\x02\x03\x04\x05')

