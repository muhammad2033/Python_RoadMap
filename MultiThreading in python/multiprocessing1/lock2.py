import multiprocessing
import time

def deposit(balance):
    for i in range(100):
        time.sleep(0.1)
        balance.value = balance.value+1  #it is in shared memory 

def withdraw(balance):
    for i in range(100):
        time.sleep(0.1)
        balance.value = balance.value -1
        
  
if __name__ =="__main__":
    balance = multiprocessing.Value('i',200)
    d = multiprocessing.Process(target = deposit, args = (balance,))        3       4
    w = multiprocessing.Process(target = withdraw, args = (balance,))        
    
    d.start() 
    w.start()
     
    d.join() 
    w.join()
    print(balance.value)
     
    print(" process is done!") 
    