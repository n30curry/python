#!/usr/bin/python

from socket import *

def start():
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(('192.168.1.21',8888))
    sock.listen(5)
    while True:
        sock.setblocking(3)
        clientsock,clientaddr = sock.accept()

        buf = clientsock.recv(1024)
        clientsock.send(buf)
        clientsock.close()
        print "+++++++++++++++++"

if __name__ == "__main__":
    start()
