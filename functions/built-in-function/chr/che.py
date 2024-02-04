# Python chr()
# In this tutorial, you will learn about the python chr() method with the help of examples.

# The chr() method converts an integer to its unicode character and returns it.

# Example

print(chr(97))
# Output: a

print(chr(98))
#  Output: b

# Run Code
# chr() Syntax
# The syntax of chr() is:

# chr(number)
# chr() Parameter
# The chr() method takes in a single parameter:

# number - an integer number in the range 0 to 1,114,111
# chr() Return Value
# The chr() method returns:

# a unicode character of the corresponding integer argument (in the range 0 to 1,114,111)
# ValueError - for an out of range integer number
# TypeError - for a non-integer argument

# Example 1: Python chr() with Integer Numbers

print(chr(97))
print(chr(65))
print(chr(1200))

# Run Code
# Output

# a
# A
# Ұ

# In the above example, we have used the chr() method to convert different integers to their corresponding unicode characters. Here,

# a is the unicode character of 97
# A is the unicode character of 65
# Ұ is the unicode character of 1200

# Example 2: chr() with Out of Range Integer

print(chr(-1000))
print(chr(1114113))

# Run Code
# Output

# ValueError: chr() arg not in range(0x110000)
# In the above example, we have provided out of range integer arguments like -1000 and 1114113 to the chr() method. This results in a ValueError.

# Example 3: chr() with Non-Integer Arguments

print(chr('Ronald'))
print(chr('Lupin'))

# Run Code
# Output

# TypeError: an integer is required (got type str)
# In the above example, we have used the chr() method with Non-Integer Arguments. This results in a TypeError.

