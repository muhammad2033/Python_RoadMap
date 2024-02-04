list = ['maaz', 'is','a', 'programmer']


for i in list:
    print(i)

print(dir(list))

name = iter(list)
print(name)

# next 

nex =next(name)
print(nex)


print(dir(name)) #return all directories


#reversed

reverse = reversed(list) #return from reverse order or last

print(next(reverse))

print(dir(list))

