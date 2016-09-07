#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')


while True:
    buf = f.readline()
    if buf == '':
        break
    print buf
