#!/usr/bin/python 

from socket import *
import sys
from select import *



def main():
    host = sys.argv[1]
    post = int(sys.argv[2])
    ADDR = (host,post)
    sockfd = socket()
    sockfd.connect(ADDR)
    while True:
        data = raw_input()
           
        if not data:
            break
        sockfd.send(data)
        data = sockfd.recv(1024)
        print data

    sockfd.close()

if __name__ == '__main__':
    main()
