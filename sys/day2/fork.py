#!/usr/bin/python

import os

pid = os.fork()

if pid == 0:
    print "child:",os.getpid()

else:
    print "parent:",os.getpid()

print "++++++++++++"
