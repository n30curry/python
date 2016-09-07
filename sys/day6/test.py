
#!/usr/bin/python 
#coding=utf-8

from socket import *
from select import *
from time import ctime

HOST = '192.168.1.21'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.bind(ADDR)
sockfd.listen(5)

inputs = [sockfd]
 
while True:
    rs,ws,es = select(inputs,[],[])
    for r in rs:
        if r is sockfd:
            connfd,addr = sockfd.accept()
            print "connected from :",addr
            inputs.append(connfd)
        else:
            
            data = r.recv(BUFSIZE)
           # except socket.error:
            #    dosconnect = True
            if not data:
                print r.getpeername(),'disconnectd'
                inputs.remove(r)
                r.close()
            else:
                r.send('[%s] :%s'%(ctime(),data))

sockfd.close()
