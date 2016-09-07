#!/usr/bin/python


for i in range(5,1001):
    
    for j in range(1,i/2):
        d = []
        if i % j ==0:
            d.append(j)
            a = len(d)
        for x in range(a):
            c = 0
            c = d[x] + c
        if c == i:
            print i

