#!/usr/bin/python
#coding=utf-8

a = raw_input()
l = a.split("-")
x = int (l[0])
y = int (l[1])
z = int (l[2])

if y >12 or y < 1:
    print"请输入正确的月份"
if x >31 or x < 1:
    print"请输入正确的日期"
if y == 1:
    print x
if y == 2:
    print 31 + z
if y == 3:
    if x % 4 ==0:
        if x > 29:
            print "请输入正确的日期"
        else:
            print 60 + z

    else:
        print


