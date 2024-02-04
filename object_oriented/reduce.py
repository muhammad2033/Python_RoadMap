from functools import reduce
red = lambda a, b : a*b #multiply from 1 to 9 consecutively 

l = [1,2,3,4,5,6,7,8,9]

print("red:",reduce(red,l))

red = lambda a, b : a+b #add from 1 to 9 consecutively 

l = [1,2,3,4,5,6,7,8,9]

print("red:",reduce(red,l))

#  here i can use the built-in function too 


l = [1,2,3,4,5,6,7,8,9]

print("red:",reduce(max,l)) 
#used to find out the max value from the list with the help of reduce function 

l = [1,2,3,4,5,6,7,8,9]

print("red:",reduce(min,l))
#used to find out the min value from the list with the help of reduce function 

