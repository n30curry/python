#!/usr/bin/python

from socket import *
import sys

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.connect(sys.argv[1],int(sys.argv[2]))

while True:
    data = raw_input('>')
    sockfd.send(data)
    data = sockfd.recv(1024)
    print data

sockfd.close()
