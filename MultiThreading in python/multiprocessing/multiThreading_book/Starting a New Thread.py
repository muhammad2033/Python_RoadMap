
                # Starting a New Thread

# To spawn another thread, you need to call the following method available in the thread
# module-
# _thread.start_new_thread ( function, args[, kwargs] )
# This method call enables a fast and efficient way to create new threads in both Linux and 
# Windows.
# The method call returns immediately and the child thread starts and calls function with 
# the passed list of agrs. When the function returns, the thread terminates.



import time 
import _thread

# define a function with thread 
def print_time(name,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count =+1
        print("%s : %s "%(name,time.ctime(time.time())) ) 
        
    # create two threads as follows 
    
try:
    _thread.start_new_thread(print_time,("thread_1:",2,)) 
    _thread.start_new_thread(print_time,("thread_2:",4,))
 
except Exception as e:
    print("error is handled :", e)
 
while 1:
    pass         