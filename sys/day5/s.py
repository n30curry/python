#!/usr/bin/python 

from socket import *

host = '192.168.1.21'
post = 7777
bufsize = 1024 
ADDR = (host,post)

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(ADDR)
while True:
    print "waiting for message"

    data,addr = sockfd.recvfrom(bufsize)
    print "client addr :",addr  
    sockfd.sendto(data,addr)

sockfd.close()
