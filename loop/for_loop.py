def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac *i
        print(f"the factorial {n} is :",fac)
    
n =int(input(" enter the number for factorial!"))   
factorial(n)
    