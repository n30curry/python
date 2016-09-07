#!/usr/bin/python 
#coding=utf-8

import MySQLdb

db = MySQLdb.connect('localhost','root','123','testdb')

cursor = db.cursor()

sql = "updata emp set sex = 'm' where name = 'list'"
#sql = "updata emp set age = age + 1 where sex = 'm'"
try:
    cursor.execute(sql)
    db.commint()
except:
    print "Error : failed updata"
    db.rollback() #回到上一次的版本

sql = "delete from emp where age > 20"

try:
    cursor.execute(sql)
    db.commint()
except:
    print "failed updata"
    db.rollback()

db.close()

