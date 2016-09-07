#!/usr/bin/python

class Node(object):
    def __init__(self,val,p = None):
        self.val = val
        self.next = p
        self.prior = p

class Linklist(object):
    def __init__(self):
        self.head = None
    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            node.prior = p
            p = p.next

    def show(self):
        p = self.head.prior
        while p!= None:
            print p.val
            p = p.prior


