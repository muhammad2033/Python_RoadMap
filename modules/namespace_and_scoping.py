money = 2000  # global variable 

def addmoney():
    
    #uncomment the following line to fix the code 
    #global money
    
    money = money + 1  # local variable 

print(money)
addmoney()
print(money)