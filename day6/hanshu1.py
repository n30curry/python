#!/usr/bin/python



def fun(n,x):
    
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * fun(n - 1,x) - (n - 1) * fun(n - 2,x))/n
print fun(4,6)
