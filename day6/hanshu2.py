#!/usr/bin/python


def fun(*l):
    j = list(l)
    for i in j:
        if i % 2 == 0:
            
            j.append(i)
            j.remove(i)
    print j 
l = [1,2,3,4,5,6,7,8,9]
fun(*l)
