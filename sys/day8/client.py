#!/usr/bin/python 

from threading import *
import MySQLdb,sys,socket


def regster(num,sockfd):
    sockfd.send(num)
    data = sockfd.recv(1024)
    while data == 'name':
        data = raw_input("input name(string) >>")
        sockfd.send(data)
        data = sockfd.recv(1024)
        if data == "ok":
            break
        else:
            print "sorry the name existe"
            continue
    passwd = raw_input("input passwd(string) >>")
    sockfd.send(passwd)
    data = sockfd.recv(1024)
    print data


def chaxun(num,sockfd):
    while True:
        sockfd.send(num)
        data = raw_input("please input danci >>")
        if data == 'quit':
            sockfd.send('quit')
            return
        sockfd.send(data)
        data = sockfd.recv(1024)
        print data


def history(num,sockfd):
    sockfd.send(num)
    data = sockfd.recv(1024)
    print data
    


def login(num,sockfd):
    while True:
        sockfd.send(num)
        name = raw_input("input name >>")
        sockfd.send(name)
        passwd = raw_input("input passwd >>")
        sockfd.send(passwd)

        data = sockfd.recv(1024)
        if data == 'ok':
            print "welcome %s"%name
            break
        else:
            print "sorry,your name or passwd is error !!! please chong xin input"

    while True:
        print '''
            ---------------command----------------
            ---1: chaxun   2: history   3: quit---
            --------------------------------------
            '''

        num = raw_input("please input command >>")

        if num not in ['1','2','3']:
            print "input error"
            sys.stdin.flush()
            continue
        if num == '1':
            chaxun(num,sockfd)
        elif num == '2':
            history(num,sockfd)
        else:
            sockfd.send('3')
            return






def main():
    host = sys.argv[1]
    post = int(sys.argv[2])
    ADDR = (host,post)
    sockfd = socket.socket()
    sockfd.connect(ADDR)

    while True:
        print '''
            -----------------command-----------------
            ---1: login     2: regster     3: quit---
            -----------------------------------------
            '''

        num = raw_input("Input command >>")

        if num not in ['1','2','3']:
            print "input error!"
            sys.stdin.flush
            continue
        elif num == '1':
            login(num,sockfd)
        elif num == '2':
            regster(num,sockfd)
        elif num == '3':
            sys.exit()
            return

if __name__ == "__main__":
    main()
    
