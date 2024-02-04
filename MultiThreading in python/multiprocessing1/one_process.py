import time
import multiprocessing

square_result = []
def square (num):
    global square_result   
    for n in num:
        print("square :" + str(n*n))
        square_result.append(n*n)
            

if __name__== "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target = square , args=(arr,))

    
    p1.start()
    
    p1.join()
    print("result :", str(square_result))  #the array is empty here 
    print("done!")

# i want to include the all square element in the array 

import time
import multiprocessing

square_result = []
def square (num):
    global square_result   
    for n in num:
        print("square :" + str(n*n))
        square_result.append(n*n)
    print("within a process :inside:"+str(square_result))  #including the elements           

if __name__== "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target = square , args=(arr,))

    
    p1.start()
    
    p1.join()
    print("outside :", str(square_result))  #the array is empty here 
    print("done!")
