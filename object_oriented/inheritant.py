class teacher :
    
    def incomeSalary(self,salary):
        self.salary = salary
        
        
    def experience(self , experiences ):
        self.experiences = experiences
        
    def displayIncome(self):
        print("income salary for teacher is :", self.salary)
     
    def displayExperience(self):
        print("the experience for teacher is :",self.experiences)   
        
class student(teacher):
    
    def incomeSalarySTD(self,salary):
        self.salary = salary
        
    def experienceSTD(self , experiences ):
        self.experiences = experiences
        
    def displayIncomeSTD(self):
        print("income salary for student is :", self.salary)
     
    def displayExperienceSTD(self):
        print("the experience for student  is :",self.experiences) 
                 
st = student()

# calling for teacher through inheritation of student 

st.incomeSalary(20000)
st.displayIncome()   

st.experience("fifteen years!!")
st.displayExperience()              

# calling for student through inheritation by itsef 


st.incomeSalarySTD(2000)
st.displayIncomeSTD()   

st.experienceSTD("two years!!")
st.displayExperienceSTD()              


# we can call the attributes of teacher with the help of calling to student 