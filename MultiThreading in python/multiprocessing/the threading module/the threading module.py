import threading
import time

exitflag = 0

class  mythread(threading.Thread):
    def __init__(self,threadId, name , counter):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.counter = counter
        
    def run(self):
        print(f"starting: {self.name}") 
        print_time(self.name,self.counter,5)
        print(f"exiting : {self.name}")
        
def print_time(threadName, delay, counter):
    while counter:
        if exitflag:
            threadName.exit()
        
        time.sleep(delay)
        print("%s :%s"%(threadName,time.ctime(time.time())))
        
        counter-=1
        
# creates two threads  
thread1 = mythread( 1 , "thread1", 1) 
thread2 = mythread( 2, "thread_2", 2 )

# start new threads

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("exiting main thread:")
        