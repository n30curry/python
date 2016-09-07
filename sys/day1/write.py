#!/usr/bin/python

import sys

l = ['haha','nihao','I love china\n']
f = open(sys.argv[1],'w')
f.write('hello world\n')
f.writelines(l)
