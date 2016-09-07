#!/usr/bin/python

import multiprocessing
import sys
from time import sleep

def worker_with(lock,stream):
    with lock:
        for i in range(5):
            sleep(1)
            stream.write('Lock acquired via with\n')

def  worker_no_with(lock,stream):
    lock.acquired()
    try:
        for i in range(5):
            sleep(1)
            stream.write('Lock acquireddirectly\n')
    finally:
        lock.release()

lock = multiprocessing.Lock()
w = multiprocessing.Process(target = worker_with,args = (lock,sys.stdout))

nw = multiprocessing.Process(target = worker_no_with,args = (lock,sys.stdout))

w.start()
nw.start()


