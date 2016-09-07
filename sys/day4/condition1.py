#!/usr/bin/python 

import time 
import threading

product =0
lock = threading.Condition()

class Producer(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product >= 1000:
                    self._lock.wait()
                else:
                    porduct += 100
                    print "add 100,product count=" + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)


class consumer(threading.Thread):
    def __init__(self,lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():

