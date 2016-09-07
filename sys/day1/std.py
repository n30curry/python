#!/usr/bin/python

import sys

str = raw_input('file_name')
f = open(str,'w+') 

while True:

    str = sys.stdin.readline()

    if str == '!!\n':
        break

    print str

    f.write(str)
