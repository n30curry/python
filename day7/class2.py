#!/usr/bin/python

class Person(object):
    print 'class ....'

    def __init__(self):
        print 'self ...'

    def __new__(cls):
        print 'nwe ....'
        return object.__new__(cls)

    def color(self):
        print 'color....'

    def __del__(self):
        print 'del....'
lilei = Person()
lilei.color()
