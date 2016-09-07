#!/usr/bin/python 

import socket,os,sys,traceback
from threading import *

host = '192.168.1.21'
port = 9999

def handler(clientsock):
    print "New child"
    print "Got connection from ",clientsock.getpeername()
    while True:
        data = clientsock.recv(1024)
        if not len(data):
            break
        clientsock.send(data)

    clientsock.close()

s = socket.socket()
s.bind((host,port))
s.listen(5)

while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    t = Thread(target = handler,args = (clientsock,))
    t.setDaemon(1)
    t.start()

s.close()
