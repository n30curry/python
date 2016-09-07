#!/usr/bin/python

import multiprocessing
import time

def stage_1(cond):
    '''perform first stage of work,then notify stage_2 to continue'''
    name = multiprocessing.current_process().name
    print 'Starting',name
    with cond:
        pront '%s done and ready for stage 2'%name
        cond.notify_all() #添加条件,wait()才会正常执行

def stage_2(cond):
    '''wait for the condition telling us stage_1 is done'''
    name = multiprocessing.current_process().name
    print 'Starting',name
    with cond:
        cond.wait()
        print '%s running'%name

if __name__ == '__main__': 
