# it converts the float and string into integers 


name = "1223459568858694"

sum1 = 3.4
sum2 = 5.6

sum = sum1+sum2

print("the float will be integer here: ",int(sum))

print("the string  will be integer here: ",int(name))


# int() Syntax
# The syntax of the int() method is:


# int(value, base [optional])
# int() Parameters
# int() method takes two parameters:


# value - any numeric-string, bytes-like object or a number
# base [optional] - the number system that the value is currently in
# int() Return Value
# The int() method returns:


# integer portion of the number - for a single argument value (any number)
# 0 - for no arguments
# integer representation of a number with a given base (0, 2 ,8 ,10,16)


# Example 2: int() with Two Arguments

# converting a string (that is in binary format) to integer
print("For 0b101, int is:", int("0b101", 2))

# converting a string (that is in octal format) to integer
print("For 0o16, int is:", int("0o16", 8))

# converting a string (that is in hexadecimal format) to integer
print("For 0xA, int is:", int("0xA", 16))

print(int("0b1111",2))   #binary from string to integer
    
    
# Run Code
# Output

# For 0b101, int is: 5
# For 0o16, int is: 14
# For 0xA, int is: 10


# Example 3: int() for custom objects

# Even if an object isn't a number, we can still convert it to an integer object.

# We can do this easily by overriding __index__() and __int__() methods of the class to return a number.

# The two methods are identical. The newer version of Python uses the __index__() method.

class Person:
    age = 23

    def __index__(self):
        return self.age

    # def __int__(self):
    #     return self.age

person = Person()

# int() method with a non integer object person
print("int(person) is:", int(person))


def maaz():
    def __init__(self,name):
        self.name = name
        print(f"the name is : {name} ")
obj = maaz()        

print(obj)    
    
    