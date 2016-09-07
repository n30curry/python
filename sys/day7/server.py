#!/usr/bin/python 

from socket import *
import sys
import threading
from select import *

class Server:
    pass


def main():
    host = sys.argv[1]
    post = int(sys.argv[2])
    ADDR = (host,post)

    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(10)
    inputs = [sockfd]
    l = []
    while True:
        rs,ws,es = select(inputs,[],[])
        for r in rs:
            print r
            if r is sockfd:
                connfd,addr = sockfd.accept()
                print "connected from :",addr
                inputs.append(connfd)
                l.append(connfd)
                print l
            else:
                try:
                    data = r.recv(1024)
                    disconnect = not data
                except socket.error:
                    disconnect = True
                if disconnect:
                    print r.getpeername(),'disconnectd'
                    inputs.remove(r)
                    l.remove(r)
                    r.close()
                else:
                    for i in l:
                        try:
                            i.send("123")
                        except:
                            print 'error'
                                

    sockfd.close()

if __name__ == '__main__':
    main()
            


        



