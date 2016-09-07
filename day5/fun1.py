#!/usr/bin/python

def fun(a):
    print "fun:",a
    print id(a)

    a = 10
    print a 
    print id(a)

b = 1
fun(b)
print id(b)

print b
