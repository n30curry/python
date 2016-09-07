#!/usr/bin/python
#coding=utf-8

a = raw_input()
l = a.split("-")
x = int (l[0])
y = int (l[1])
z = int (l[2])
s = 0

p = [range(1,32),range(1,29),range(1,32),range(1,31),range(1,32),range(1,31),range(1,32),range(1,32),range(1,31),range(1,32),range(1,31),range(1,32)]
m = [range(1,32),range(1,30),range(1,32),range(1,31),range(1,32),range(1,31),range(1,32),range(1,32),range(1,31),range(1,32),range(1,31),range(1,32)]

if y > 12 or y <= 0:
    print"请输入正确日期"
else:  
    if x % 4 == 0 and x % 100 != 0:
        if 0 < z < 32:
            y -= 1
            while y > 0:
                y -= 1
                s = len(m[y]) + s
            print s + z
        else:
            print "请输入正确日期"
    else:
        if 0 < z < 32:
            y -= 1
            while y > 0:
                y -= 1
                s = len(p[y]) + s
            print s + z
        else:
            print "请输入正确日期"
