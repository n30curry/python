#!/usr/bin/python

class Protect:
    def __init__(self):
        self.job = 'teacher'
        self.__name = 'cainiao'

    def __python(self):
        print "I Love Python"

    def code(self):
        print "Which language do you like"
        self.__python()

if __name__ == '__main__':
    p = Protect()
    print p.job
    #print p.__name
    p.code()
