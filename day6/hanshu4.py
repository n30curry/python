#!/usr/bin/python



def fun(a):
    b = list(a)
    c = b.count(' ')
    d = b.count('-')
    for i in range(c):
        b.remove(' ')
    for j in range(d):
        b.remove('-')
    e = ''.join(b)
    print e


while True :
    a = raw_input()
    if not len(a):
        break
    fun(a)
