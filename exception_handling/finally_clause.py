try:
    name = open("finally.txt","w")
    try:
    
        name.write("this is a program for finally clause!!\n i started loving football")
    finally:
        print("this line must be printed here")
        print(" as well this line ")
        name.close()
except IOError:
    print("error!!!!")        