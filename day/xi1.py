#!/usr/bin/python

a = [1,1]
i = 0
z = 0

while i < 10:
    i += 1
    
    s = a[z] + a[z + 1]
    a.append (s)
    z += 1
print a
