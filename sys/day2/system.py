#!/usr/bin/python

import os

print "start"
os.system('ls -l')
fp = os.popen('ls -l','r')
fp.read()

