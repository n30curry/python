#!/usr/bin/python
#coding=utf-8
import signal
import time

signal.alarm(5) #5秒后向自身发送终止信号
while True:
    time.sleep(1)
    print "wait....."

# 第6行 会在内核中生成一个记录,在到达这个条件时会调用这个记录,这就是异步通信.
