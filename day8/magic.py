#!/usr/bin/python


class A():
    def __getattr__(self,name):
        pass
    

        
    
a = A()
a.x
a.x = 7

print a.x
print a.__dict__
