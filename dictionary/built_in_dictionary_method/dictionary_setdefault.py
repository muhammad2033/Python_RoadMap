dict = {'Name': 'maaz' , "hy" : 'Zara', 'Age': 7} 

print (" return the value for the given key: ",dict.get('Age',None)) #7

print (" return the value for the given key: ",dict.get('Name',None)) # maaz

print (" return the value for the given key: ",dict.get('where',None)) # none ,coz the  key(where) is not in the dictionary

print (" return the value for the given key: ",dict.get('why',None)) # maaz

# it is quite similar to the get(), it is used to return the key' value in the dictionary if it is not present in the
# list , so it will return the default None 

# so it takes two arguments one will be default None