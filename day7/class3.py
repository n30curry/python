#!/usr/bin/python

class parents():
    name = '1'

    def fun(self):
        print 'hello'
class pp():
    name = 'ti'
    age = 25

class child(parents,pp):
    pass

child = child()
print child.name
print child.age
child.fun()
