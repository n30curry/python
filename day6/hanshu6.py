#!/usr/bin/python

n = input()

def fun(n):
    l = [1,2,3,4,5,6,7,8,9]
    for i in range(n):
        b = l[8]
        l.remove(b)
        l.insert(0,b)
    print l

fun(n)
