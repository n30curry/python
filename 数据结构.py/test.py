#!/usr/bin/python

from linklist import *

a = LinkList()
a.initlist([1,2,3,4,5,6])
a.show()
a.insert(6,100)
a.show()
a.remove(4)
a.show()
a.find(3)
a.instead(2,200)
a.show()
a[1]
a[0] = 1000
a.show()
