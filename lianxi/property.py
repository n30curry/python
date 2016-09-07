#!/usr/bin/python 

def outer(fun):
    def wrapper():
        print"hello"
        fun()
        print "world"
    return wrapper

@outer
def Func1():
    print "func1"

Func1()
