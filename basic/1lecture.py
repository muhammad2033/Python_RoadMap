                        # basic
from tkinter import Variable


a = 10; n=20 ;c= 20; sum = a+n+c #we can write multiple statements in a single line

print(a,n,c,"the result is",sum)


a=b=c=1
print(a)            #multiple assignment
print(b)
print(c)


age , salary, average = 23,3333,3.4  # other way to declare Variables
print(age)
print(salary)
print(average)

# for deleting extra or multiple variables

a = 12; b = 23; c=44


del c   #deleting c value here
sum =a+b
print(sum)

# python's list

list = ["maaz", 23,24,22,2.3,"khan" ]
print(list[0:3])   #slice oprator (o to 2 index) 

# pytho's tuple

tuple = ("maaz", 23,24,22,2.3,"khan" )
print(tuple[0:3])   #slice oprator (o to 2 index)    

# python's dict
dict = {"maaz":2,"saad":"khan" }
print(dict["saad"])   #slice oprator (o to 2 index) 


# second way


dict = {
        
        1:"maaz" ,
        2:   3
            
            }

print(dict[1],dict[2])
print(dict.values())
print(dict.keys())

a = 60
print(bin(a))
