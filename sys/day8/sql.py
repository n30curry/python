#!/usr/bin/python 
#coding=utf-8

import MySQLdb

#打开数据库链接
use = raw_input("用户名:")
passwd = raw_input("密  码:")

db = MySQLdb.connect('localhost',use,passwd,'testdb')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print "database version :%s"%data
cursor.execute("drop table if exists newtab")

sql = "create table newtab(id int not null,name char(20),age int ,income float)"

cursor.execute(sql)

sql = "insert into newtab (id,name,age,income) values ('1','mac',20,8.8)"


try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


db.close()
