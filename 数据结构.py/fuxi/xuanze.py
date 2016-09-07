#!/usr/bin/python

l = [32,23,1,13,34,22,21,5,4,23,21,22]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print l
