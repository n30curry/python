#!/usr/bin/python 

from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    sockfd.sendto(data,ADDR)
    data,addr = sockfd.recvfrom(BUFSIZE)
    print data

sockfd.close()
    

