cities = ['peshawar','northompton','new york']
country = ['pakistan','england','USA']

z = zip(cities,country) #return zip objects
print(z)


# zip connects two dictionary's list 

for i in z :
    print(i)
    
d = { city :country for city ,country in zip (cities,country)}    
print (d) # in dictionary form 