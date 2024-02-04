import time 
def adding(number):
    print("calculate the two number :")
    for n in number :

        time.sleep(0.5)
        print("number:",n+n)


def subtracting(number):
    print("calculate the two number :")
    for n in number :

        time.sleep(0.5)
        print("number:",n-n)



def square(number):
    print("calculate the square number :")
    for n in number :

        time.sleep(0.5)
        print("number:",n*n)
        

def cube(number):
    print("calculate the cube number :")
    for n in number :

        time.sleep(0.5)
        print("number:",n*n*n)
        
arr = [2,4,6,8,10]

t = time.time()
adding(arr)
subtracting(arr)
square(arr)                
cube(arr)       

print("time taken:",time.time()-t)         
print("everything goes well without multithreading:")