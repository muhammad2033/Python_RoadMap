# share data between processes using array and value 

import multiprocessing

def square(number, result):
    for idx, n in enumerate(number):
        result[idx] = n*n

if __name__=="__main__":
    number = [2 , 3 , 4 , 5]
    result = multiprocessing.Array('i',4) 
    p1 = multiprocessing.Process(target = square , args=(number,result ))
    
    p1.start()
    
    p1.join()
    
    print(result[:])       