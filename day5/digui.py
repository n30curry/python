#!/usr/bin/python

def aa(n):
    if n <= 1:
        return 1
    return(n * aa(n - 1))

r = aa(5)

print('5! = %d'%r)

