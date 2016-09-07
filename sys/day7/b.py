#!/usr/bin/python

class A:
    def __init__(self,name):
        self.name = name

    def __getattr__(self,name):
        pass
a = A('lilei')
print a.name
a.gender ='man'
a.x
print a.__dict__

b = A('mimi')
print b.gender
