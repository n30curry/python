#!/usr/bin/python 

class A:
    def __getattr__(self,dfdfdf):
        print "You use getattr"

    def __setattr__(self,name,value):
        self.__dict__[name] = value
        print "You use setattr"
a = A()
a.x = 7

b = A()
print b.x
b.dddr
print a.__dict__
b.dddr = 'hello world'
