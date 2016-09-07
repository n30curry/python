#!/usr/bin/python

class A():
    def __getattr__(self,name):
        pass

a = A()
a.c = 'hello world'
print a.c
print a.__dict__
