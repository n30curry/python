#!/usr/bin/python

a = 1
for i in range(5,100):
    for j in range (2,i/2):
        if i % j == 0:
            a = 0
            break
        else:
            a = 1
    if a == 1:
        print i
    
