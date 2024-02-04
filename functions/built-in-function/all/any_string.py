# Example 3: How all() works with Python dictionaries?
# In the case of dictionaries, if all keys (not values) are true or the dictionary is empty, all() returns True. Else, it returns false for all other cases..

s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))

dict = {
    'name ':'maaz',
    False  : 0
}
print(all(dict))

# returns False