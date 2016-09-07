#!/usr/bin/python

from socket import *
from select import *

host = '192.168.1.21'
port = 9999
s = socket()
s.bind((host,port))
s.listen(5)

p = poll()
p.register(s)
fdmap = {s.fileno():s}

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = s.accept()
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(c)
                del fdmap[fd]
            else:
                fdmap[fd].send('recive message')

s.close()
