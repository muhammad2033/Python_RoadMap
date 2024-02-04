import threading
import time

count = 0
lock = threading.Lock()

def increment():
    global count
    lock.acquire()
    try:
        count += 1
    finally:
        lock.release()

threads = []
for i in range(10):
    t = threading.Thread(target=increment)
    time.sleep(2)
    print(i)
    
    threads.append(t)
    
    t.start()

for t in threads:
    t.join()

print(count) # output: 10