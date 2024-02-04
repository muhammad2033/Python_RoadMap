import threading
import time 


class mythread(threading.Thread):
    def __init__(self, threadId,name , counter):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        
        
        self.name = name
        self.counter = counter
    
    def run(self):
        print("stating:"+self.name)    #checking 
        
        # gets lock the sychrnoize thread 
        threadLock.acquire()   
        print_time(self.name, self.counter, 4)
        
        # free  lock  to release next thread
        
        threadLock.release()
        
def print_time(threadName, delay, counter)    :
    while  counter:
        time.sleep(delay)
        print("%s : %s " %(threadName, time.ctime(time.time())))
        counter -=1
        
threadLock = threading.Lock()

threads = []


# create the  new threads
thread1 = mythread(1,"thread_1",0)
thread2 = mythread(2,"thread_2",0)

# start the new thread 

thread1.start()
thread2.start()


# add threads to thread list 
threads.append(thread1)
threads.append(thread2)
# wait for all threads to complete 

for t in threads:

    t.join()
print("exiting the main thread")