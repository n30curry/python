#!/usr/bin/python

from time import sleep
import threading

def music():
    print "+++++++++"
def move():
    print "--------"
t1 = threading.Thread(target = music)
t2 = threading.Thread(target = move)
t1.start()
t2.start()
