                    # Python callable()
# The callable() method returns True if the object passed appears callable. If not, it returns False.

# The syntax of callable() is:

# callable(object)
# callable() Parameters
# callable() method takes a single argument object.

# Return value from callable()
# callable() method returns:

# True - if the object appears callable
# False - if the object is not callable.
# It important to remember that, even if callable() is True, call to the object may still fail.

# However, if callable() returns False, call to the object will certainly fail.

# Example 1: How callable() works?

x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))

# Run Code
# Output

# False
# True

# Here, the object x is not callable. And, the object y appears to be callable (but may not be callable).

# Example 2: Callable Object 

class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))

# Run Code
# Output

# True

# The instance of Foo class appears to be callable (and is callable in this case).

class Foo:
  def __call__(self):
    print('Print Something')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()

# Run Code

# Example 3: Object Appears to be Callable but isn't callable.

class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))

# Run Code
# Output

# True
# The instance of Foo class appears to be callable but it's not callable. The following code will raise an error.

class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()

# Run Code
# Output

# True
# Traceback (most recent call last):
# File "", line 10, in 
# TypeError: 'Foo' object is not callable