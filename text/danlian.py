#!/usr/bin/python

class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class linklist():
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
