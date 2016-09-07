#!/usr/bin/python

with open('hold','w') as f:
    f.write('begin\n')
    f.seek(1000,2)
    f.write('end\n')
