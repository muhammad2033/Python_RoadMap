# import time

# def calc_square(number):
#     start = time.time()
#     result = []
#     for number in number:
#         result.append(number*number)
#     end = time.time()
#     print("calc_square took " +str((end-start)*1000) + " mil sec")   
#     return result    


# def calc_cube(number):
#     start = time.time()
#     result = []
#     for number in number:
#         result.append(number*number*number)
#     end = time.time()
#     print("calc_cube took " +str((end-start)*1000) + " mil sec")   
#     return result    

# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)

# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
                                
                                # decorator (nested function)

import time

def time_it(func):
    def wrapper(*args, **Kwargs):
        start = time.time()
        func(*args,**Kwargs)
        end = time.time()
        print(func.__name__+" took " + str ((start - end )*1000) + " mil sec")
        return func(*args,**Kwargs)
    return wrapper

@time_it
def calc_square(number):
    result = []
    for number in number:
        result.append(number*number)
    return result    

@time_it
def calc_cube(number):
    result = []
    for number in number:
        result.append(number*number*number)
    return result    

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
