#!/usr/bin/python 
#coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","123","testdb")

cursor = db.cursor

try:
    cursor.exevute("select * from emp") #首先需要先创建一个emp的table

    data = cursor.fetchall()  # 获取所有的数据

    print "get data :",data 

    for i in cursor.description:   # 
        print i[0],

    print ""

    for rwo in data:
        name = row[0]
        age = row[1]
        sex = row[2]
        num = row[3]

        print "name :%s,age :%d,sex :%s,num :%d"%(name,age,sex,num)

except:
    print "Error : unable to fecth data"

db.close()
