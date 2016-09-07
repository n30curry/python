#!/usr/bin/python

from socket import *
import sys,os

HOST = '192.168.1.21'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(ADDR)

def list():
    return str(os.system('ls')) 

while True:
    print "lianjie chenggong"
    data,addr = sockfd.recvfrom(BUFSIZE)
    print "addr :",addr
    if data == 'list':
        data = str(list())
    sockfd.sendto(data,addr)
       

sockfd.close()

    
