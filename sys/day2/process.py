#!/usr/bin/python

import multiprocessing
import time
import os

def worker(t,l):
    while True:
        time.sleep(t)
        print "worker"
        time.sleep(l)
        print "+++++"
    return

p = multiprocessing.Process(target = worker,name = 'myprocess',args = (0.5,0.5))
p.start()
print p.pid
print p.name
print p.is_alive()

print os.getpid()
print os.getppid()
