import time 
import threading


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
t1 = threading.Thread(target=adding,args = (arr,))
t2 = threading.Thread(target=subtracting,args = (arr,))

t3 = threading.Thread(target=square,args = (arr,))
t4 = threading.Thread(target=cube,args = (arr,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("time taken:",time.time()-t)         
print("everything goes well with multithreading:")