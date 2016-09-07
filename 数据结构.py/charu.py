#!/usr/bin/python

def charu(l):
    for i in range(1,len(l)):
        while i > 0 and l[i-1] > l[i]:
            l[i-1],l[i] = l[i],l[i-1]
            i -= 1
    print l
l = [5,2,6,8,56,33,21,1]
charu(l)
