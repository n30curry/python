#!/usr/bin/python

class A(object):
    a = 1
    b = 2
    def fun1(self):
        print "fun1"

    def fun2(self):
        print "fun2"

a1 = A()
a1.c = 1
a1.addr  = 'hello world'
print a1.addr
print a1.__dict__
a2 = A()
#print a2.c
print a2.addr
