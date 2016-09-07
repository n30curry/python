#!/usr/bin/python
#coding=utf-8

l = [[1,2,3,4],[5,6,7,18],[9,0,10,11]]

a = l[0][0]

for i in range(0,3):
    for j in range(0,4):
        if  a < l[i][j]:
            a = l[i][j]
            x = i
            y = j
print "zuidashi%d,weizhishil[%d][%d]"%(a,x,y) 
