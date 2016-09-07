#!/usr/bin/python

def aa(l,b):
    l = list(l)
    a = len(l)
    d = []
    e = []
    if b >= 0 and b < a:
        for i in range(b):
           c = l[i:i+1]
           d =  d + c
        
        for j in range(a-b-1):
            f = l[a-1-j:a-j]
            e = f + e
            

    l = d + e
    print l

aa([1,2,3,4,5,6],2)
aa([1,2,3,22,44,13],4)

           
        


