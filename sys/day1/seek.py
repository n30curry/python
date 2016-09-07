#!/usr/bin/python

f = open('new','w+')
f.write('hello world')

f.flush()

print f.tell()
f.seek(0)
s = f.read()
print s
