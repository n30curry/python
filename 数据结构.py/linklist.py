#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)

        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def show(self):
        p = self.head.next

        while p != None:
            print p.val,
            p = p.next
        print ""

    def getlength(self):
        p = self.head
        length = 0

        while p.next != None:
            length += 1
            p = p.next

        return length
    def insert(self,index,val):
        if index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head

        j = 0
        while j < index:
            p = p.next
            j += 1

        node = Node(val,p.next)
        p.next = node 

    def remove(self,val):
        p = self.head
        if val < 0 or val > self.getlength():
            print "index is error"
            return
        j = 0 
        while j < val:
            j += 1
            p = p.next
        p.next = p.next.next

    def find(self,val):
        p = self.head
        if val < 0 or val > self.getlength():
            print "index is error"
            return
        j = 0
        while j < val:
            j += 1
            p = p.next
        print  p.next.val 

    def instead(self,index,val):
        self.remove(index)
        self.insert(index,val)

    def __getitem__(self,key):
        return self.find(key)

    def __setitem__(self,key,val):
        return self.instead(key,val)
