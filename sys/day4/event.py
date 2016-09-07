#!/usr/bin/python

import threading
from time import sleep,ctime

def wait_for_event(e):
    '''wait for the event to be set befor doing anything'''
    print "wait for event starting"
    event_is_set = e.wait()
    print "event setl:%s"%event_is_set

def wait_for_event_timeout(e,t):
    '''wait t seconds and then timeout'''
    while not e.isSet():
        print "wait for event timeout starting"
        event_is_set = e.wait(t)
        print"event set2:%s"%event_is_set
        if event_is_set:
            print "processing event"
        else:
            print "doing other work"

e = threading.Event()
t1 = threading.Thread(name = 'block',target = wait_for_event,args = (e,))
t1.start()
t2 = threading.Thread(name = 'nonblock', target = wait_for_event_timeout,args = (e,3))
t2.start()

print "waiting before calling event.set()"
sleep(4)
e.set()
print "event is set"
