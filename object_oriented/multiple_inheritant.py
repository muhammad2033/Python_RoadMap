class teacher :
    
    def incomeSalary(self,salary):
        self.salary = salary
        
        
    def experience(self , experiences ):
        self.experiences = experiences
        
    def displayIncome(self):
        print("income salary for teacher is :", self.salary)
     
    def displayExperience(self):
        print("the experience for teacher is :",self.experiences)   
        
class student:
    
    def incomeSalarySTD(self,salary):
        self.salary = salary
        
    def experienceSTD(self , experiences ):
        self.experiences = experiences
        
    def displayIncomeSTD(self):
        print("income salary for student is :", self.salary)
     
    def displayExperienceSTD(self):
        print("the experience for student  is :",self.experiences) 

class  robot(teacher , student ):
    
    def working_time (self,speed):
        
        self.speed = speed
    def robustnes(self, robust):
        self.robust = robust 
        
    def displaySpeed(self):
        print("the speed is :",self.speed)        
     
       
    def displayrobustness(self):
        print("the robustness is :",self.robust)        
                         
rob = robot()

# calling for teacher through inheritation of robot

rob.incomeSalary(20000)
rob.displayIncome()   

rob.experience("fifteen years!!")
rob.displayExperience()              

# calling for student through inheritation of robot 


rob.incomeSalarySTD(2000)
rob.displayIncomeSTD()  
rob.experienceSTD("two years!!")
rob.displayExperienceSTD()              


rob.working_time("very fast upto millions")
rob.displaySpeed()
rob.robustnes("very good and strong ,working well and easily!")
rob.displayrobustness()
# we can call the attributes of teacher and student  with the help of  calling to robot `` 
