# Example 2: Using any() on Python Strings

# At east one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))


dict = {
    'name ':'maaz',
    False  : 0
}
print(any(dict))

# returns true