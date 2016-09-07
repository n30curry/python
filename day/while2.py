#!/usr/bin/python
#coding=utf-8

import random

i = 1
while i < 5:
    num = random.randint(0,9)
    a = raw_input()    
    i += 1
    n = 5 - i
    if 'a' == 'num':
        print "猜对了"
        break
    if 'a' > 'num':
        print "猜大了 正确的是%d 还有%d次"%(num,n)
    if 'a' < 'num':
        print "猜小了 正确的是%d  还有%d次"%(num,n)
