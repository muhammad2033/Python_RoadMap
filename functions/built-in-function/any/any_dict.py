

# Example 3: Using any() with Python Dictionaries
# In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, any() returns False. If at least one key is true, any() returns True.

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))