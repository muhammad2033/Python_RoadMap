class maaz:
    def __init__(self,name , age , experience):
        self.name  = name  
        self.age = age  
        self.experience = experience
        
    def display(self):
        print(f"{self.name} is a programmar his  age is almost  {self.age} years ,\n and his experience is a little bit almost {self.experience} years  \n") 
        
 
obj1 = maaz("muhammad maaz",22,2)
obj1.display()
 
obj2= maaz("muhammad habib",24,4)
obj2.display()
  
obj3 = maaz("muhammad musawwir",26,6 )
obj3.display()
     
        