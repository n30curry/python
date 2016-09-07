#!/usr/bin/python

def MaoPao(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j],l[j+1] = l[j+1],l[j]
    print l

a = [1,2,5,343,34,63,3,65,43,765,77]
MaoPao(a)


def xuanze(l):
    for i in range(len(l) - 1):
        min = i
        for j in range(i+1,len(l)):
            if l[min] > l[j]:
                min = j
        if i != min:
            l[i],l[min] = l[min],l[i]
    print l
xuanze(a) 


def charu(l):
    for i in range(1,len(l)):
        s = l[i]
        j = i
        while j > 0 and l[j - 1] > s:
            l[j] = l[j -1]
            j -= 1
            l[j] = s
    print l 

