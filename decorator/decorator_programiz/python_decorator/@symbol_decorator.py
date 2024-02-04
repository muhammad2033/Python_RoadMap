# Instead of assigning the function call to a variable,
# Python provides a much more elegant way to achieve this functionality using the @ symbol. For example,

def make_pretty(func):
    def inner():
        print(" this is inner function !")
        
        func()

    return inner

@make_pretty

def ordinary():
    print(" this is ordinary person ")
    
ordinary()    
