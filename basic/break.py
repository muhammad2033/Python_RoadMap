# start = int (input(" enter the value for initialization:"))
# condition = int (input(" enter the value for condition:"))

for i in range(6):
    if (i<2):
        print("good")
        break #when it comes true
    else:
        print("the statement is false:")
else:
    print("the statement doesnt match:")        
    
    
    
#     # break for while loop 
from tkinter import E


var = 10
while (var > 0):
    print(" the var is : ", var)
    var = var-1
    if var ==6:
        print("stop at :",var)
        
    
        break  # for termination
else:
    print("there is no such sort of letter:")
        
    
    # break for for loop
    
for i in range(8):
    if i == 4:
        print(f"the value will stop at 4: {i}:")
        break
    
else:
    print("it wont stop ")  
    print(i)       
   
num = int (input(" enter the number for num: "))    

list = [33,44,55,66,77,82,893,43,52,23,63,73,73]

for number in list:
    if number ==num:
        print(f"the value is present in the list :{num}  ")
      
        break  
    # else:
        # print("yelling!!!")
else:
    print(f"the value isnt present in the list : {num} ")
            
print("good bye!")            
            
        