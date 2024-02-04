import multiprocessing
import time

def square (num,q):
    for n in num:
        q.put(n*n)
        
        
if __name__== "__main__":
    arr = [2,3,4,5]
    
    time.sleep(2)
    q =multiprocessing.Queue()
    p = multiprocessing.Process(target = square , args=(arr,q))

    
    p.start()
    
    p.join()
    
    while q.empty() is False:
        print(q.get())
