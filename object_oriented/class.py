class employee:
    "common  base class all  employees"
    empCount = 0
    
    def __init__(self, name , salary):
        self.name = name 
        self. salary = salary 
        employee.empCount +=1
        
    def  displayCount(self):
        print("total employee %d"%employee.empCount)
        
    def displayEmployee(self):
        print("name :",self.name,"salary:",self.salary)    
        

# this would create first object of employee class        
emp1 = employee("maaz ",2000)    #instantiation of the class     

# this would create second object of employee class         
emp2 = employee("saad ",4000)         #instantiation of the class

# calling portion 

emp1.displayEmployee() 
emp2.displayEmployee()

emp2.displayCount()
emp1.displayCount()

                # or
print("total employee %d"%employee.empCount)                


# adding the new attributes   
emp1.salary = 20000

emp1.name = "muhammad"

emp1.displayEmployee() 
emp2.displayEmployee()


# # deleting the attributes  

del emp1.name
del emp1.salary


emp1.displayEmployee() 
emp2.displayEmployee()  #error coz of deleting the attributes 