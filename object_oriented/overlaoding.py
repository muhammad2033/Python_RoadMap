# class vector:
#     def __init__(self,a ,b):
#         self.a = a 
#         self.b = b
         
#     def __str__(self):
#         return ('vector(%d,%d)' %(self.a,self.b))
    
#     def __add__(self, other):
#         return vector(self.a+other.a,self.b +other.b)
    
 
# v1 = vector (3,6) 
# v2 = vector (5,6)
# print(v1+v2)
 
class student :
    
    def __init__(self,salary,name):
        self.salary = salary
        self.name  = name         
        
    def __str__(self) :
        return("the salary is :",self.salary," the name is :",self.name)
    
    
obj = student(20000,"muhammad maaz")
print(obj)  