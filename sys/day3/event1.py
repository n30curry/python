#!/usr/bin/python 
 
import multiprocessing
import time

def wait_for_event(e):
    '''waiting for the event to be set befor doing anything'''
    print  'wait_for_event :starting'
    e.wait()
    print 'wait_for_event:e.id_set()->',e.is_set()

def wait_for_event_timeout(e,t):
    '''wait seconds and then timeout'''
    print 'wait_for_event_timeout : starting'
    e.wait(t)
    print 'wait_for_event_timeout : e.is_set()->',e.is_set()

if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = 'block',target = wait_for_event,args = (e,))
    w1.start()

    w2 = multiprocessing.Process(name = 'non-block',target = wait_for_event_timeout,args = (e,2))
    w2.start()

    print 'main :waiting before calling Event.set()'
    time.sleep(4)
    e.set()
    print 'main : event is set'
