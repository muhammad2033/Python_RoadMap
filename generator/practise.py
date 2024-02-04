def Generator():
    yield "maaz"
    yield "is"
    yield " a "
    yield "great"
    yield "programmer"
    
r = Generator()    
iter = iter(r)
print(iter)
 
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


# 2nd way of printing
 
for c in Generator():
    print(c)

