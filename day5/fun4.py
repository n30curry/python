#!/usr/bin/python

a = 1
def fun():
    global a 
    a += 1

    print "in",a
    
fun()
print"out",a
