#!/usr/bin/python

from socket import *
import sys

host = sys.argv[1]
post = int(sys.argv[2])
bufsize = 1024
ADDR = (host,post)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    sockfd.sendto(data,ADDR)
    data,ADDR = sockfd.recvfrom(bufsize)
    print data

sockfd.close()
