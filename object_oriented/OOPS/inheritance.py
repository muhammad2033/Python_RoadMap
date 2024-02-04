class Parent: # define parent class

    parentAttr = 100

    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
class Child(Parent): # define child class

    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ('Calling child method')

c = Child() # instance of child
c.childMethod() # child calls its method
c.parentMethod() # calls parent's method
c.setAttr(200) # again call parent's method
c.getAttr() # again call parent's method

print(isinstance(c,Child)) #returns true if the instance is correctly given,otherwise false

print(issubclass(Child,Parent))#returns true if the subclass is correctly given,otherwise false