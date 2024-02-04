import queue 
import threading
import time

exitFlag = 0
class mythread(threading.Thread):
    def __init__(self, threadId,threadname, q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadname = threadname   
        self.q = q
        
    def run(self):
        print("starting :", self.name)
        process_data(self.name,self.q)
        

def process_data(threadname,q):
    while not exitFlag:
        queuelock.acquire()
        if not workQueue.empty():
            data = q.get()
            queuelock.release()
            print("%s processing  %s "%(threadname, data))     
        
        else:
            queuelock.release()
            
            time.sleep(1)
            
threadlist = ["thread-1","thread-2","thread-3"] 
namelist = ["one ","two", " three", "four", "five", "six"]

queuelock = threading.Lock()
workQueue = queue.Queue (10)

threads = []
threadId = 1

# create new threads 
for tname in threadlist :
    thread  = mythread(threadId, tname, workQueue)           
    thread.start()
    threads.append(thread)
    threadId += 1
    
# fill the queue

queuelock.acquire()
for word in namelist:     
    workQueue.put(word)

queuelock.release()

# wait for queue  to empty 
while not workQueue.empty():
    
    pass

# notify it's time to exit 
exitFlag= 1

# wait for all threads to complete  
for t in  threads :
    t.join()

print("exiting the main thread:")