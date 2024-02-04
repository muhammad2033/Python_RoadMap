dict = { "name" :"maaz", "rollno" : 2033} 

del dict["name"] # one by one keys can be deleted

print("dict['name']",dict["name"])  # error,typeError,coz its deleted 

dict.clear()

print("dict.clear()",dict) # we can delete all entries in dictionary 

del dict

print("dict:",dict) # we can delete an entire dictionary 

#one more way, we can delete an entire dictionary 

del(dict)

print(dict)