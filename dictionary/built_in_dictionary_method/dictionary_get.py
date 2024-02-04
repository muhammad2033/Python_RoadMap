dict = {'Name': 'maaz' , "hy" : 'Zara', 'Age': 7} 

print (" return the value for the given key: ",dict.get('Age')) #7

print (" return the value for the given key: ",dict('Name')) # maaz

print (" return the value for the given key: ",dict.get('where')) # none ,coz the  key(where) is not in the dictionary


# it is used to get the values of the given keys of dictionary.If the keys are not in dictionary,so it returns
# none 
