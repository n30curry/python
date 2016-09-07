#!/usr/bin/python
#coding=utf-8
import sys,os
from time import sleep

(r,w) = os.pipe() # 返回两个整数,代表两个管道描述符,第一个代表读,第二个代表写

pid = os.fork()
if pid < 0:
    print "fail to fork"
elif pid == 0:
    print "child :"   #读 和 写  本身就是阻塞函数
    os.close(w)   #关闭掉w文件描述符
    r = os.fdopen(r)     #将文件描述符转换为文件对象,不写默认是读权限
    while True:
        buf = r.readline()
        print "buf :",buf
        sys.stdout.flush()
    print "child close"
else:
    print "parent :"
    os.close(r)
    w = os.fdopen(w,'w') 
    while True:
        buf = sys.stdin.readline() #固定用法在终端输入

        w.write(buf)
        w.flush()
#无名管道 只能在父子进程里通信
