# # it is an ordered collection of unique elemnets 

# set = {"maaz",2,5,5,5,0,False,"yes "}
# print(set)
# print(type(set)) #set

# # we are not supposed to use the empty set ,then that will be dictionary 
# a = {}
# print(type(a))  #dictionary

#                             #  initialization
# a = set()
# a.add(1)
# a.add(2)
# print(a)

#set doesnt allow support indexing 
#set doesnt allow replicate or redundant value

number = {1,2,3,4,5,5,6,8,0}

set = set(number)
print(set)

set.add(99)
print(set)

number1 = {1,2,3,4,5,5,55,6,8,0}

new = number-number1
print(new) #difference

new = number|number1
print(new) #union

new = number&number1
print(new)          #intersection


number1 = {1,2,3,4,5,5,55,6,8,0}
print(number1)