# first property is ; dont need to put two keys in one dictionary,so it will return the last same key 

dict = { "name" :"maaz", "rollno" : 2033,"name":"saad"} 

print("property first is :",dict["name"]) # returns the last one "saad"


# second property is ; keys must be immutable This means you can use strings, numbers or tuples as dictionary keys,
#  but something like ['key'] is not allowed.

dict = { "name" :"maaz", "rollno" : 2033,"name":"saad"} 

print("property second is :",dict["name"]) # returns error,unhashabe type:list



