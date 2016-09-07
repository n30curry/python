#!/usr/bin/python

class A():
    def __getattr__(self,name):
        pass
    def __setattr__(self,name,value):
        self.__dict__[name] = value
    pass
a = A()
a.x
a.x = 7
print a.__dict__
print a.x
