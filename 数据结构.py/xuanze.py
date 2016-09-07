#!/usr/bin/python

def xuanze(l):
    for i in range(len(l)):
        for j in range(1+i,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    print l
a = [3,54,23,12,4,12,1321,43]
xuanze(a)

