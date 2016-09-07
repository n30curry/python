#!/usr/bin/python

def maopao(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

    print l

a = [1,3,3,432,234,213,11,123,45]
maopao(a)
