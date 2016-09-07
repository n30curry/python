#!/usr/bin/python

__metaclass__ = type
class Person():

    def __init__(self):
        self.height = 100

    def about(self,name):
        print '{} is about {}'.format(name,self.height)

class Girl(Person):
    def __init__(self):
        
        self.zhong = 50

    def about (self,name):
        print name self.height self.zhong

chan = Girl()
chan.about('diaochan')

