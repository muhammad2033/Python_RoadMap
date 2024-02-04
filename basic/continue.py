# continue for for loop 

for i in range(11):
    if i==8:
        continue
    print(" the 8 number wont be executed here:",i)
  
  
  
   
num = int (input(" enter the number for num: "))    

list = [33,44,55,66,77,82,893,43,52,23,63,73,73]

for number in list:
    if number ==num:
        continue  
        
    print(f"the value is present in the list :{number}  ")
      
    # else:
        # print("yelling!!!")
else:
    print(f"the value isnt present in the list : {number} ")
            
print("good bye!")            
                