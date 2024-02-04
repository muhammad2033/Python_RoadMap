# Open a file

fo = open("next.txt", "r")

print ("Name of the file: ", fo.name)

for index in range(7):
    
    line = next(fo)
    
    print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()

                            # another example 

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)

x = next(mylist)
print(x)

x = next(mylist)
print(x)

x = next(mylist,"pineapple")
print(x)
