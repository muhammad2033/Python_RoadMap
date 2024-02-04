import time
import multiprocessing

def square (num):
    for n in num:
        time.sleep(1)
        print("square :" + str(n*n))
        

def cube(num):
    for n in num:
        time.sleep(1)
        print("cube :" + str (n*n*n))


if __name__== "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target = square , args=(arr,))
    p2 = multiprocessing.Process(target = cube   , args=(arr,))

    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("done!")
