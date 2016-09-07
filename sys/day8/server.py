#!/usr/bin/python 

from threading import *
import MySQLdb,sys,socket
import time


def regster(conn):
    db = MySQLdb.connect('localhost','root','123','student')
    cursor = db.cursor()
    while True:
        conn.send("name")  
        name = conn.recv(1024)
        sql = "select * from usr where name = '%s'"%name
        cursor.execute(sql)
        data = cursor.fetchone()

        if not data:
            conn.send('ok')
            break
        else:
            conn.send("sorry the name existe")

    passwd = conn.recv(1024)
    sql = "insert into usr value('%s','%s')"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        conn.send("sorry operation failed")
        db.rollback()
        return

    conn.send("regster OK")
    db.close()


def chaxun(conn,db,cursor):

    while True:
        data = conn.recv(1024)
        if data == 'quit':
            return
        a = open('dict.txt','r')
        b = a.readlines()
        c = len(data)

        for i in b:
            if data == i[0:len(data)]:
                conn.send(i)
                t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
                i = i + t
                sql = "insert into cha value('%s')"%i
                cursor.execute(sql)
                db.commit()
                db.close()
                a.close()
                break




def login(conn):
    db = MySQLdb.connect('localhost','root','123','student')
    cursor = db.cursor()
    while True:
        name = conn.recv(1024)
        passwd = conn.recv(1024)
    
        sql = "select * from usr where name = '%s' and passwd = '%s'"%(name,passwd)
        cursor.execute(sql)
        data = cursor.fetchone()

        if data == None:
            conn.send("gg")
            continue
        else:
            conn.send('ok')
            break
    
    while True:
        data = conn.recv(1024)
        if data == '1':
            chaxun(conn,db,cursor)
        elif data == '2':
            sql = "select * from cha"
            cursor.execute(sql)
            data = cursor.fetchone()
            data = str(data)
            conn.send(data)
        else:
            db.close()
            return
    

def handler(conn):
    print "Got connection from ",conn.getpeername()
    while True:
        data = conn.recv(1024)
        if data == '1':
            login(conn)
        elif data == '2':
            regster(conn)





def main():
    host = sys.argv[1]
    post = int(sys.argv[2])
    ADDR = (host,post)
    sockfd = socket.socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)


    while True:
        try:
            conn,addr = sockfd.accept()
        except KeyboardInterrupt:
            raise
        except:
            continue

        t = Thread(target = handler, args = (conn,))
        t.start()

    sockfd.close()

if __name__ == '__main__':
    main()
