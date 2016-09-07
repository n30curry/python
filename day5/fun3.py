#!/usr/bin/python

def fun(a,b):
    print a,b

fun(1,2)

fun (a=3,b=2)

l=[3,5]
fun(*l)

s = {'b':3,'a':6}
fun(**s)
