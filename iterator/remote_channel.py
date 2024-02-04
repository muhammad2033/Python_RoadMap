class remote_channel:
    def __init__(self, channel) :
        
        self.channel = channel  
        self.index = -1
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        self.index +=1
        if self.index == len(self.channel):
            raise StopIteration("iteration")
        
        
        return self.channel[self.index]   
   
r = remote_channel(['HBO','ARY','TSL','ptv'])
iter = iter(r)

print( next(iter) )   
print( next(iter) )   
print( next(iter) )   
print( next(iter) )   
print( next(iter) )   