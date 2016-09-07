#!/usr/bin/python

def fib(demo):
    
    a , b = 1 , 2
    while a < demo:
        
        yield a 
        a = a + b
        print "********"
for i in fib(10):
    print i

print dir(fib)
