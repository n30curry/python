#!/usr/bin/python
#coding=utf-8

import multiprocessing
import time

class clockprocess(multiprocessing.Process):
    def __init__(self,value):
        multiprocessing.Process.__init__(self)
        self.value = value

    def run(self):
        n = 5
        while n>0:
            print "the time is {}",format(time.ctime())
            time.sleep(self.value)
            n -= 1
p = clockprocess(3)
p.start()
# 继承multiprocessing.Process()的init 函数  创建子进程后在类里会找run函数自动运行

