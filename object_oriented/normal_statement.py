class employee:
    "anything can be here inside the string !!"
    empcount = 0
    
    
    def __init__(self, salary , name) :
        self.salary = salary 
        self.name = name 
        employee.empcount +=1  #incrementation 
    
    def displaycount (self):
        print("total employees: %d"%employee.empcount)
            
    def displayEmployee(self):
        print("salary :",self.salary,"name:",self.name ) 
        
    
emp1 = employee(3000,'maaz')           
emp2 = employee(5000,"saad")           

emp1.displayEmployee()
emp2.displayEmployee()

print("total employees: %d"%employee.empcount)

# normal statement in python 
  
# del emp1.salary  then false , if deletes  

w = hasattr(emp1,'salary')
print(w) #returns True if the attribute exits 'salary'

x= getattr(emp1,'salary') 
x= getattr(emp1,'name')   #it gets the attribute 'salary'
print(x)

y = setattr(emp1,'salary',6000)
y = setattr(emp2,'salary',9000) # it sets the attribute 'salary'

emp1.displayEmployee()
emp2.displayEmployee()

z = delattr(emp1,'salary') #it deletes the attribute "salary"

emp1.displayEmployee()  #error , coz it's deleted



