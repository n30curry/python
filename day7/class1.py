#!/usr/bin/python

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fuse(self,color):
        print "%s is %s and %d sui"%(self.name,color,self.age)

lilei = Person('lilei',20)
lilei.fuse('red')
