class employee:
    "If we dont assign the string to anything , so by employee.__doc__ we can call "
    empcount = 0
    
    def __init__(self, name , salary,age):
        self.name = name 
        self.salary = salary 
        self.age = age
        employee.empcount += 1
        
    def displayEmployee(self):
             
        print("name :",self.name,"salary :",self.salary,"age :",self.age)
        
    def displaycount(self):
        print("total employees %d:" %employee.empcount)
        
emp1 = employee("muhammad maaz",20000,23)            
emp2 = employee("muhammad saad",30000,25)            

emp1.displayEmployee()
emp2.displayEmployee()

print("total employees are : %d" %employee.empcount)

print("employee.__doc__:",employee.__doc__)
print("employee.__name__:",employee.__name__)
print("employee.__module__:",employee.__module__)
print("employee.__bases__:",employee.__bases__)
print("employee.__dict__:",employee.__dict__)


def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function()


