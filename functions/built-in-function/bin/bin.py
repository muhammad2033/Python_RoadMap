# The bin() method converts a specified integer number to its binary representation and returns it.

# Example

number = 15

# convert 15 to its binary equivalent 
print('The binary equivalent of 15 is', bin(number))

# Output: The binary equivalent of 15 is 0b1111


# bin() Syntax
# The syntax of bin() method is:


# bin(number)
# bin() Parameter
# The bin() method takes in a single parameter:


# number - an integer whose binary equivalent is calculated
# bin() Return Value
# The bin() method returns:


# the binary string equivalent to the given integer
# TypeError for a non-integer argument


# Example 2: Python bin() with a Non-Integer Class
class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def func():
        return apple + orange + grapes
        
print('The binary equivalent of quantity is:', bin(Quantity()))


# Output

# TypeError: 'Quantity' object cannot be interpreted as an integer

# Here, we have passed an object of class Quantity to the bin() method and got a TypeError.

# This is because we have used a non-integer class.

# Note: We can fix the TypeError above by using the Python __index__() method with a non-integer class.


# Example 3: bin() with __index__() for Non-Integer Class

class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
        
print('The binary equivalent of quantity is:', bin(Quantity()))


str = "name of the user"
name  = len(str)
print(bin(name))

# string cant be cnverted 

float = 2.3
print(bin(float))

#string cant be as well as float 

