#!/usr/bin/python
#coding=utf-8

#只有读段或写端 是阻塞的
#只有都有再回冲破这种阻塞
#只有写 没有读 会导致管道破裂
#只有读 没有写 会继续读 但读出的东西是空的,
#这是因为 它会把管道里的东西读出来

from time import sleep
import os

try:
    os.mkfifo('fifo')
except:
    print "fifo exist"

f = open('fifo','w')
while True:
    sleep(1)
    f.write('hello\n')
    f.flush
