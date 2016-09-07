#!/usr/bin/python

l = [lambda x:x ** 2,lambda x: x ** 3,lambda x: x ** 4]

for f in l:
    print f(2)

print l[0](3)

