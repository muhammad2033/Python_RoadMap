class employee:
    'THERE IS  THE PROGRAM FOR DESTRUCTOR! '
    
    def __init__(self,salary = 0, age=0):
        self.salary = salary 
        self.age = age
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed!")
 
emp1 =  employee()
emp2 = emp1
emp3 = emp1      

print(id(emp1),id(emp2),id(emp3))  #  print the ids of the object                               

del emp1
del emp2
del emp3

class Employee:
     
    # Initializing
    def __init__(self):
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
del obj

# it is used to delete the object of the class 